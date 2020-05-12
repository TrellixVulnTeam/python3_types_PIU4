from typing import Any

NMCLI_DEVICE: str
NMCLI_LINETERMINATOR: str
NMCLI_DELIMITER: str
logger: Any

def _network_device() -> str: ...
def _network_device_is_enabled(device: str) -> bool: ...
def _network_device_enable(device: str, enable: bool) -> Any: ...
def test_network_disconnect(group: str = ...) -> None: ...
