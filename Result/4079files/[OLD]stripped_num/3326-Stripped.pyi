# (generated with --quick)

from typing import Any, Callable, Dict, Tuple, TypeVar

BadStation: Any
Cloud: Any
Icing: Any
Location: Any
Number: Any
PirepData: Any
Timestamp: Any
Turbulance: Any
Units: Any
_dict_handlers: Dict[str, Callable[[Any], Any]]
_handlers: Dict[str, Tuple[str, Callable[[Any], Any]]]
_units: Any
core: Any
static: Any

_T0 = TypeVar('_T0')

def _aircraft(item: _T0) -> _T0: ...
def _altitude(item) -> Any: ...
def _clouds(item) -> list: ...
def _icing(item) -> Any: ...
def _location(item) -> Any: ...
def _number(item) -> Any: ...
def _remarks(item: _T0) -> _T0: ...
def _root(item) -> Dict[str, Any]: ...
def _time(item) -> Any: ...
def _turbulance(item) -> Any: ...
def _wx(item) -> Dict[str, Any]: ...
def parse(report) -> Any: ...