# (generated with --quick)

from typing import Any, TypeVar, Union

CLASS: Any
Symbol: Any
SymbolCONST: Any
SymbolTYPE: Any
TYPE: Any
numbers: module

_TSymbolNUMBER = TypeVar('_TSymbolNUMBER', bound=SymbolNUMBER)

class SymbolNUMBER(Any):
    __doc__: str
    class_: Any
    lineno: Any
    t: str
    type_: Any
    value: Union[float, int]
    def __add__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __and__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __div__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, value, lineno, type_ = ...) -> None: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __mod__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __mul__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __or__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __radd__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __rand__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __rdiv__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __repr__(self) -> str: ...
    def __rmod__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __rmul__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __ror__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __rsub__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __rtruediv__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __str__(self) -> str: ...
    def __sub__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...
    def __truediv__(self: _TSymbolNUMBER, other) -> _TSymbolNUMBER: ...

def _get_val(other) -> Any: ...
