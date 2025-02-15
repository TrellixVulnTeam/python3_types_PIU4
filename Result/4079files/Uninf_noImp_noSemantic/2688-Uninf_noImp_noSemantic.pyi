from typing import Any

pytestmark: Any

def tls_smtp_client(request: Any, event_loop: Any, hostname: Any, port: Any): ...
def tls_smtpd_server(request: Any, event_loop: Any, bind_address: Any, port: Any, smtpd_class: Any, smtpd_handler: Any, server_tls_context: Any): ...
async def test_tls_connection(tls_smtp_client: Any, tls_smtpd_server: Any) -> None: ...
async def test_starttls(smtp_client: Any, smtpd_server: Any) -> None: ...
async def test_starttls_init_kwarg(hostname: Any, port: Any, smtpd_server: Any) -> None: ...
async def test_starttls_connect_kwarg(smtp_client: Any, smtpd_server: Any) -> None: ...
async def test_starttls_with_explicit_server_hostname(smtp_client: Any, hostname: Any, smtpd_server: Any) -> None: ...
async def test_starttls_not_supported(smtp_client: Any, smtpd_server: Any, smtpd_class: Any, smtpd_response_handler_factory: Any, monkeypatch: Any) -> None: ...
async def test_starttls_advertised_but_not_supported(smtp_client: Any, smtpd_server: Any, smtpd_class: Any, smtpd_response_handler_factory: Any, monkeypatch: Any) -> None: ...
async def test_starttls_disconnect_before_upgrade(smtp_client: Any, smtpd_server: Any, smtpd_class: Any, smtpd_response_handler_factory: Any, monkeypatch: Any) -> None: ...
async def test_starttls_invalid_responses(smtp_client: Any, smtpd_server: Any, event_loop: Any, smtpd_class: Any, smtpd_response_handler_factory: Any, monkeypatch: Any, error_code: Any) -> None: ...
async def test_starttls_with_client_cert(smtp_client: Any, smtpd_server: Any, valid_cert_path: Any, valid_key_path: Any) -> None: ...
async def test_starttls_with_invalid_client_cert(smtp_client: Any, smtpd_server: Any, invalid_cert_path: Any, invalid_key_path: Any) -> None: ...
async def test_starttls_cert_error(event_loop: Any, smtp_client: Any, smtpd_server: Any) -> None: ...
async def test_tls_get_transport_info(tls_smtp_client: Any, tls_smtpd_server: Any, hostname: Any, port: Any, event_loop: Any) -> None: ...
async def test_tls_smtp_connect_to_non_tls_server(tls_smtp_client: Any, smtpd_server: Any, event_loop: Any, hostname: Any, port: Any) -> None: ...
async def test_tls_connection_with_existing_sslcontext(tls_smtp_client: Any, tls_smtpd_server: Any, client_tls_context: Any) -> None: ...
async def test_tls_connection_with_client_cert(tls_smtp_client: Any, tls_smtpd_server: Any, hostname: Any, valid_cert_path: Any, valid_key_path: Any) -> None: ...
async def test_tls_connection_with_cert_error(event_loop: Any, tls_smtp_client: Any, tls_smtpd_server: Any) -> None: ...
