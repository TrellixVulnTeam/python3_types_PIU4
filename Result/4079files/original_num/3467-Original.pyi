# (generated with --quick)

from typing import Any

MAX_STOP_DURATION: int
TSDBClient: Any
TSDBConnectProtocols: Any
TSDBNotAlive: Any
ValidationError: Any
pytest: Any
time: module

def _test_sending_metric(client) -> None: ...
def test_bad_chars_send(http_client) -> None: ...
def test_bad_value_send(http_client) -> None: ...
def test_check_tsdb_alive() -> None: ...
def test_host_tag(telnet_client) -> None: ...
def test_http_client_close(http_client) -> None: ...
def test_no_tag_send(http_client) -> None: ...
def test_predefined_metrics(http_client3) -> None: ...
def test_send_metric_through_http(http_client) -> None: ...
def test_send_metric_through_telnet(telnet_client) -> None: ...
def test_telnet_client_close(telnet_client) -> None: ...
