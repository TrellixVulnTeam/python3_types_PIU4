"""
TLS and STARTTLS handling.
"""
import copy
import socket
import ssl

import pytest

from aiosmtplib import (
    SMTP,
    SMTPConnectError,
    SMTPException,
    SMTPResponseException,
    SMTPServerDisconnected,
    SMTPStatus,
)


pytestmark = pytest.mark.asyncio()


@pytest.fixture(scope="function")
def tls_smtp_client(request, event_loop, hostname, port):
    tls_client = SMTP(hostname=hostname, port=port, use_tls=True, validate_certs=False)

    return tls_client


@pytest.fixture(scope="function")
def tls_smtpd_server(
    request,
    event_loop,
    bind_address,
    port,
    smtpd_class,
    smtpd_handler,
    server_tls_context,
):
    def factory():
        return smtpd_class(
            smtpd_handler,
            hostname=bind_address,
            enable_SMTPUTF8=False,
            tls_context=server_tls_context,
        )

    server = event_loop.run_until_complete(
        event_loop.create_server(
            factory,
            host=bind_address,
            port=port,
            ssl=server_tls_context,
            family=socket.AF_INET,
        )
    )

    def close_server():
        server.close()
        event_loop.run_until_complete(server.wait_closed())

    request.addfinalizer(close_server)

    return server


async def test_tls_connection(tls_smtp_client, tls_smtpd_server):
    """
    Use an explicit connect/quit here, as other tests use the context manager.
    """
    await tls_smtp_client.connect()
    assert tls_smtp_client.is_connected

    await tls_smtp_client.quit()
    assert not tls_smtp_client.is_connected


async def test_starttls(smtp_client, smtpd_server):
    async with smtp_client:
        response = await smtp_client.starttls(validate_certs=False)

        assert response.code == SMTPStatus.ready

        # Make sure our state has been cleared
        assert not smtp_client.esmtp_extensions
        assert not smtp_client.supported_auth_methods
        assert not smtp_client.supports_esmtp

        # Make sure our connection was actually upgraded. ssl protocol transport is
        # private in UVloop, so just check the class name.
        assert "SSL" in type(smtp_client.transport).__name__

        response = await smtp_client.ehlo()
        assert response.code == SMTPStatus.completed


async def test_starttls_init_kwarg(hostname, port, smtpd_server):
    smtp_client = SMTP(
        hostname=hostname, port=port, start_tls=True, validate_certs=False
    )

    async with smtp_client:
        # Make sure our connection was actually upgraded. ssl protocol transport is
        # private in UVloop, so just check the class name.
        assert "SSL" in type(smtp_client.transport).__name__


async def test_starttls_connect_kwarg(smtp_client, smtpd_server):
    await smtp_client.connect(start_tls=True, validate_certs=False)

    # Make sure our connection was actually upgraded. ssl protocol transport is
    # private in UVloop, so just check the class name.
    assert "SSL" in type(smtp_client.transport).__name__

    await smtp_client.quit()


async def test_starttls_with_explicit_server_hostname(
    smtp_client, hostname, smtpd_server
):
    async with smtp_client:
        await smtp_client.ehlo()

        await smtp_client.starttls(validate_certs=False, server_hostname=hostname)


async def test_starttls_not_supported(
    smtp_client, smtpd_server, smtpd_class, smtpd_response_handler_factory, monkeypatch
):
    response_handler = smtpd_response_handler_factory(
        "{} HELP".format(SMTPStatus.completed)
    )
    monkeypatch.setattr(smtpd_class, "smtp_EHLO", response_handler)

    async with smtp_client:
        await smtp_client.ehlo()

        with pytest.raises(SMTPException):
            await smtp_client.starttls(validate_certs=False)


async def test_starttls_advertised_but_not_supported(
    smtp_client, smtpd_server, smtpd_class, smtpd_response_handler_factory, monkeypatch
):
    response_handler = smtpd_response_handler_factory(
        "{} please login".format(SMTPStatus.tls_not_available)
    )
    monkeypatch.setattr(smtpd_class, "smtp_STARTTLS", response_handler)

    async with smtp_client:
        await smtp_client.ehlo()

        with pytest.raises(SMTPException):
            await smtp_client.starttls(validate_certs=False)


async def test_starttls_disconnect_before_upgrade(
    smtp_client, smtpd_server, smtpd_class, smtpd_response_handler_factory, monkeypatch
):
    response_handler = smtpd_response_handler_factory(
        "{} Go for it".format(SMTPStatus.ready), close_after=True
    )
    monkeypatch.setattr(smtpd_class, "smtp_STARTTLS", response_handler)

    async with smtp_client:
        with pytest.raises(SMTPServerDisconnected):
            await smtp_client.starttls(validate_certs=False)


async def test_starttls_invalid_responses(
    smtp_client,
    smtpd_server,
    event_loop,
    smtpd_class,
    smtpd_response_handler_factory,
    monkeypatch,
    error_code,
):
    response_handler = smtpd_response_handler_factory("{} error".format(error_code))
    monkeypatch.setattr(smtpd_class, "smtp_STARTTLS", response_handler)

    async with smtp_client:
        await smtp_client.ehlo()

        old_extensions = copy.copy(smtp_client.esmtp_extensions)

        with pytest.raises(SMTPResponseException) as exception_info:
            await smtp_client.starttls(validate_certs=False)

        assert exception_info.value.code == error_code
        # Make sure our state has been _not_ been cleared
        assert smtp_client.esmtp_extensions == old_extensions
        assert smtp_client.supports_esmtp is True

        # Make sure our connection was not upgraded. ssl protocol transport is
        # private in UVloop, so just check the class name.
        assert "SSL" not in type(smtp_client.transport).__name__


async def test_starttls_with_client_cert(
    smtp_client, smtpd_server, valid_cert_path, valid_key_path
):
    async with smtp_client:
        response = await smtp_client.starttls(
            client_cert=valid_cert_path,
            client_key=valid_key_path,
            cert_bundle=valid_cert_path,
            validate_certs=True,
        )

        assert response.code == SMTPStatus.ready
        assert smtp_client.client_cert == valid_cert_path
        assert smtp_client.client_key == valid_key_path
        assert smtp_client.cert_bundle == valid_cert_path


async def test_starttls_with_invalid_client_cert(
    smtp_client, smtpd_server, invalid_cert_path, invalid_key_path
):
    async with smtp_client:
        with pytest.raises(ssl.SSLError):
            await smtp_client.starttls(
                client_cert=invalid_cert_path,
                client_key=invalid_key_path,
                cert_bundle=invalid_cert_path,
                validate_certs=True,
            )


async def test_starttls_cert_error(event_loop, smtp_client, smtpd_server):
    # Don't fail on the expected exception
    event_loop.set_exception_handler(None)

    async with smtp_client:
        with pytest.raises(ssl.SSLError):
            await smtp_client.starttls(validate_certs=True)


async def test_tls_get_transport_info(
    tls_smtp_client, tls_smtpd_server, hostname, port, event_loop
):
    async with tls_smtp_client:
        compression = tls_smtp_client.get_transport_info("compression")
        assert compression is None  # Compression is not used here

        peername = tls_smtp_client.get_transport_info("peername")
        assert peername[0] in ("127.0.0.1", "::1")  # IP v4 and 6
        assert peername[1] == port

        sock = tls_smtp_client.get_transport_info("socket")
        assert sock is not None

        sockname = tls_smtp_client.get_transport_info("sockname")
        assert sockname is not None

        cipher = tls_smtp_client.get_transport_info("cipher")
        assert cipher is not None

        peercert = tls_smtp_client.get_transport_info("peercert")
        assert peercert is not None

        sslcontext = tls_smtp_client.get_transport_info("sslcontext")
        assert sslcontext is not None

        sslobj = tls_smtp_client.get_transport_info("ssl_object")
        assert sslobj is not None


async def test_tls_smtp_connect_to_non_tls_server(
    tls_smtp_client, smtpd_server, event_loop, hostname, port
):
    # Don't fail on the expected exception
    event_loop.set_exception_handler(None)

    with pytest.raises(SMTPConnectError):
        await tls_smtp_client.connect()
    assert not tls_smtp_client.is_connected


async def test_tls_connection_with_existing_sslcontext(
    tls_smtp_client, tls_smtpd_server, client_tls_context
):
    await tls_smtp_client.connect(tls_context=client_tls_context)
    assert tls_smtp_client.is_connected

    assert tls_smtp_client.tls_context is client_tls_context

    await tls_smtp_client.quit()
    assert not tls_smtp_client.is_connected


async def test_tls_connection_with_client_cert(
    tls_smtp_client, tls_smtpd_server, hostname, valid_cert_path, valid_key_path
):
    await tls_smtp_client.connect(
        hostname=hostname,
        validate_certs=True,
        client_cert=valid_cert_path,
        client_key=valid_key_path,
        cert_bundle=valid_cert_path,
    )
    assert tls_smtp_client.is_connected

    await tls_smtp_client.quit()
    assert not tls_smtp_client.is_connected


async def test_tls_connection_with_cert_error(
    event_loop, tls_smtp_client, tls_smtpd_server
):
    # Don't fail on the expected exception
    event_loop.set_exception_handler(None)

    with pytest.raises(SMTPConnectError) as exception_info:
        await tls_smtp_client.connect(validate_certs=True)

    assert "CERTIFICATE_VERIFY_FAILED" in str(exception_info.value)
