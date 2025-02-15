# (generated with --quick)

from typing import Any, TypeVar, Union

JSONPO: Any
JSONSD: Any
json: module

AnyStr = TypeVar('AnyStr', str, bytes)

class Configure(Any):
    FilePath: Any
    Manager: Any
    __doc__: str
    autologin: Any
    def __deserialize__(self, obj) -> None: ...
    def __init__(self, filepath = ...) -> None: ...
    def __serialize__(self) -> str: ...
    def get_auto_login(self) -> Any: ...
    def save(self) -> None: ...
    def set_auto_login(self, autlogin) -> None: ...

def expanduser(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
