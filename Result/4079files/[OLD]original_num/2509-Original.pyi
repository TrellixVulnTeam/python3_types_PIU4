# (generated with --quick)

from typing import Any, List, Optional

AcceptConnection: Any
CLIENT: Any
CloseReason: Any
Event: Any
Extension: Any
FakeExtension: Any
Headers: Any
RejectConnection: Any
RejectData: Any
RemoteProtocolError: Any
Request: Any
WSConnection: Any
generate_accept_token: Any
h11: Any
normed_header_dict: Any
pytest: Any
test_handshake_response_broken_connection_header: Any
test_handshake_response_broken_upgrade_header: Any

def _make_connection_request(request) -> Any: ...
def _make_handshake(response_status: int, response_headers, subprotocols: Optional[List[str]] = ..., extensions: Optional[list] = ..., auto_accept_key: bool = ...) -> list: ...
def _make_handshake_rejection(status_code: int, body: Optional[bytes] = ...) -> list: ...
def test_broken_handshake() -> None: ...
def test_connection_request() -> None: ...
def test_connection_request_additional_headers() -> None: ...
def test_connection_request_parametrised_extension() -> None: ...
def test_connection_request_simple_extension() -> None: ...
def test_connection_request_simple_extension_no_offer() -> None: ...
def test_connection_request_subprotocols() -> None: ...
def test_handshake() -> None: ...
def test_handshake_bad_extension() -> None: ...
def test_handshake_bad_subprotocol() -> None: ...
def test_handshake_extra_accept_headers() -> None: ...
def test_handshake_rejection() -> None: ...
def test_handshake_rejection_with_body() -> None: ...
def test_handshake_response_missing_websocket_key_header() -> None: ...
def test_handshake_with_extension() -> None: ...
def test_handshake_with_subprotocol() -> None: ...
def test_protocol_error() -> None: ...
