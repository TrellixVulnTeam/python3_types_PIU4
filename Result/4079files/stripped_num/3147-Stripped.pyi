# (generated with --quick)

from typing import Any, TypeVar

DEVICE_INTERFACE: Any
Device: Any
GATTCharacteristic: Any
GATTDescriptor: Any
GATTService: Any
GATT_CHARACTERISTIC_INTERFACE: Any
GATT_DESCRIPTOR_INTERFACE: Any
GATT_SERVICE_INTERFACE: Any
GLib: Any
OBJECT_MANAGER_INTERFACE: Any
PROPERTIES_INTERFACE: Any
SERVICE_NAME: Any
find_adapter: Any
get_known_devices: Any
logging: module
pickle: module
print_device: Any
pydbus: Any

_TSniffer = TypeVar('_TSniffer', bound=Sniffer)

class Sniffer(object):
    __doc__: str
    _log: logging.Logger
    adapter: Any
    attempt_connection: Any
    backup_interval: Any
    output_path: Any
    queued_connections: int
    queueing_interval: Any
    registry: Any
    threshold_rssi: Any
    def __enter__(self: _TSniffer) -> _TSniffer: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool: ...
    def __init__(self, output_path = ..., backup_interval = ..., resume = ..., attempt_connection = ..., threshold_rssi = ..., queueing_interval = ...) -> None: ...
    def _cb_backup_registry(self) -> bool: ...
    def _cb_connect_check(self) -> bool: ...
    def _cb_interfaces_added(self, sender, obj, iface, signal, params) -> None: ...
    def _cb_interfaces_removed(self, sender, obj, iface, signal, params) -> None: ...
    def _cb_properties_changed(self, sender, obj, iface, signal, params) -> None: ...
    def _connect(self, device) -> None: ...
    def _find_device(self, device) -> Any: ...
    def _find_device_by_path(self, path) -> Any: ...
    def _register_characteristic(self, path, characteristic) -> None: ...
    def _register_descriptor(self, path, descriptor) -> None: ...
    def _register_device(self, device) -> None: ...
    def _register_service(self, path, service) -> None: ...
    def run(self) -> None: ...
