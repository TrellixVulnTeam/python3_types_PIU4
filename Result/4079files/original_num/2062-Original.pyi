# (generated with --quick)

from typing import Any
import wpi.reg

GetObject: Any
LPR: int
RAW: int
_LOCAL_PORT_REG_KEY: str
copy: module
hooky: Any
logging: module
reg: module
time: module
win32serviceutil: Any

class LocalPort:
    value: Any
    def __init__(self, value = ...) -> None: ...

class Ports(Any):
    _localregtips: wpi.reg.Tips
    _old_localregtips: Any
    _tcpipobj: Any
    _tcpipobjs: dict
    _tcpipobjs_to_del: list
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key) -> Any: ...
    def __init__(self, computer = ..., account = ...) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def make_a_localport(self, name) -> LocalPort: ...
    def make_a_tcpipport(self, name) -> TCPIPPort: ...
    def save(self) -> None: ...

class TCPIPPort:
    def __eq__(self, other) -> bool: ...
    def __getattr__(self, key) -> Any: ...
    def __init__(self, win32obj = ...) -> None: ...
    def __setattr__(self, key, value) -> None: ...
    def _load(self, win32obj) -> dict: ...
    def save_to(self, win32obj) -> None: ...
    def update(self, other) -> None: ...
