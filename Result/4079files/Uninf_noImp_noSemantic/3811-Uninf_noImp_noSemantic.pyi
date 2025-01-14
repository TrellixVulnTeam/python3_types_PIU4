from gi.repository import GObject, Gconnect
from helper import DbusProxy
from typing import Any

class BatteryProxy(DbusProxy):
    PACKET_TYPE_REQUEST: str = ...
    charge: int = ...
    is_charging: Any = ...
    def __init__(self, proxy: Any) -> None: ...
    def introspection_xml(self): ...
    def formatted_receive(self, body: Any) -> None: ...
    def m_dbus_charge(self, parameters: Any, invocation: Any, *user_data: Any) -> None: ...
    def m_dbus_isCharging(self, parameters: Any, invocation: Any, *user_data: Any) -> None: ...
    def m_dbus_request(self, parameters: Any, invocation: Any, *user_data: Any) -> None: ...

class BatteryPlugin(GObject.Object, Gconnect.PluginPlugin):
    __gtype_name__: str = ...
    CLASS_PROXY: Any = ...
    device: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def formatted_receive(self, body: Any) -> None: ...
    proxy: Any = ...
    worker: Any = ...
    def do_activate(self, name: str) -> Any: ...
    def do_deactivate(self) -> None: ...
