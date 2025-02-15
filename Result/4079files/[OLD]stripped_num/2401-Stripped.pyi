# (generated with --quick)

from typing import Any, TypeVar, Union

InvalidData: Any

_T0 = TypeVar('_T0')

def require_bool(value: _T0, convert = ..., allow_none = ...) -> Union[bool, _T0]: ...
def require_dict(value: _T0, key_type = ..., value_type = ..., allow_none = ...) -> Union[dict, _T0]: ...
def require_int(value: _T0, allow_none = ...) -> Union[int, _T0]: ...
def require_list(value: _T0, item_type = ..., allow_none = ...) -> Union[list, _T0]: ...
def require_str(value: _T0, convert = ..., allow_none = ...) -> Union[str, _T0]: ...
