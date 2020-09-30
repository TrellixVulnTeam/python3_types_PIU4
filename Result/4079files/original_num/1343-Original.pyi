# (generated with --quick)

import typing
from typing import Any, Tuple, Type, TypeVar

DATAS: Any
LightCurveBase: Any
Mapping: Type[typing.Mapping]
attr: module
np: module
os: module
requests: module
shutil: module

_T1 = TypeVar('_T1')

class Bunch(typing.Mapping):
    __doc__: str
    _data: dict
    def __dir__(self) -> dict_keys: ...
    def __getattr__(self, key) -> Any: ...
    def __getitem__(self, key) -> Any: ...
    def __init__(self, data = ..., **kwargs) -> None: ...
    def __iter__(self) -> `dictionary-keyiterator`: ...
    def __len__(self) -> int: ...
    def __setstate__(self, state) -> None: ...

class Data(typing.Mapping):
    __doc__: str
    bands: Any
    data: Any
    description: Any
    ds_name: Any
    id: Any
    metadata: Any
    def __getitem__(self, k) -> Any: ...
    def __init__(self, id, ds_name, description, bands, metadata, data) -> None: ...
    def __iter__(self) -> generator: ...
    def __len__(self) -> int: ...

class LightCurve(Any, typing.Mapping):
    def __getitem__(self, k) -> Any: ...
    def __iter__(self) -> generator: ...
    def __len__(self) -> int: ...

def clear_data_home(data_home = ...) -> None: ...
def fetch(url, dest: _T1, force = ...) -> Tuple[bool, _T1]: ...
def get_data_home(data_home = ...) -> Any: ...