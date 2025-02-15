# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

_T0 = TypeVar('_T0')

class BMA2X2:
    __doc__: str
    _resolution: float
    acc_addr: Any
    chip_id: Any
    i2c: Any
    def __init__(self, i2c, addr) -> None: ...
    def _read_accel(self, addr) -> Any: ...
    def compensation(self, active: _T0 = ...) -> Union[bool, _T0]: ...
    def get_filter_bw(self) -> Any: ...
    def get_range(self) -> int: ...
    def set_filter_bw(self, freq) -> None: ...
    def set_range(self, accel_range) -> None: ...
    def temperature(self) -> Any: ...
    def x(self) -> Any: ...
    def xyz(self) -> Tuple[Any, Any, Any]: ...
    def y(self) -> Any: ...
    def z(self) -> Any: ...

def _twos_comp(val, bits = ...) -> Any: ...
def sleep(secs: float) -> None: ...
