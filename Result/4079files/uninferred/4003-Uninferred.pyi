import subprocess
from typing import Any, Callable, List, Optional

class WinWiFi:
    @classmethod
    def get_profile_template(cls: Any) -> str: ...
    @classmethod
    def netsh(cls: Any, args: List[str], timeout: int=..., check: bool=...) -> subprocess.CompletedProcess: ...
    @classmethod
    def get_profiles(cls: Any, callback: Callable=...) -> List[str]: ...
    @classmethod
    def gen_profile(cls: Any, ssid: str=..., auth: str=..., encrypt: str=..., passwd: str=..., remember: bool=...) -> str: ...
    @classmethod
    def add_profile(cls: Any, profile: str) -> Any: ...
    @classmethod
    def scan(cls: Any, refresh: bool=..., callback: Callable=...) -> List[WiFiAp]: ...
    @classmethod
    def get_interfaces(cls: Any) -> List[WiFiInterface]: ...
    @classmethod
    def get_connected_interfaces(cls: Any) -> List[WiFiInterface]: ...
    @classmethod
    def disable_interface(cls: Any, interface: str) -> Any: ...
    @classmethod
    def enable_interface(cls: Any, interface: str) -> Any: ...
    @classmethod
    def connect(cls: Any, ssid: str, passwd: str=..., remember: bool=...) -> Any: ...
    @classmethod
    def disconnect(cls) -> None: ...
    @classmethod
    def forget(cls: Any, *ssids: str) -> Any: ...

class WiFiAp:
    @classmethod
    def parse_netsh(cls: Any, raw_data: str) -> WiFiAp: ...
    _ssid: Any = ...
    _auth: Any = ...
    _encrypt: Any = ...
    _bssid: Any = ...
    _strength: Any = ...
    _raw_data: Any = ...
    def __init__(self, ssid: str=..., auth: str=..., encrypt: str=..., bssid: str=..., strength: int=..., raw_data: str=...) -> None: ...
    @property
    def ssid(self) -> str: ...
    @property
    def auth(self) -> str: ...
    @property
    def encrypt(self) -> str: ...
    @property
    def bssid(self) -> str: ...
    @property
    def strength(self) -> int: ...
    @property
    def raw_data(self) -> str: ...

class WiFiConstant:
    STATE_CONNECTED: str = ...
    STATE_DISCONNECTED: str = ...

class WiFiInterface:
    @classmethod
    def parse_netsh(cls: Any, raw_data: str) -> WiFiInterface: ...
    _name: Any = ...
    _state: Any = ...
    _ssid: Any = ...
    _bssid: Any = ...
    def __init__(self, name: str=..., state: str=..., ssid: Optional[str]=..., bssid: Optional[str]=...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def ssid(self) -> Optional[str]: ...
    @ssid.setter
    def ssid(self, value: str) -> Any: ...
    @property
    def bssid(self) -> Optional[str]: ...
    @bssid.setter
    def bssid(self, value: str) -> Any: ...