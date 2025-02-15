# (generated with --quick)

from typing import Any, Callable, Dict, Generator

CustomValueError: Any
FUNCS: Dict[str, Callable[[Any, Any], Any]]
InvalidOperator: Any

def contains(item, array) -> bool: ...
def equal(a, b) -> Any: ...
def find(obj, query, operator_str: str = ...) -> Generator[Any, Any, None]: ...
def greater(a, b) -> Any: ...
def greater_equal(a, b) -> Any: ...
def has_key(key, value) -> bool: ...
def in_(array, value) -> bool: ...
def less(a, b) -> Any: ...
def less_equal(a, b) -> Any: ...
def matcher_level(value, query, operator_str: str) -> Any: ...
def resolve(func, query_value, value, operator_str: str) -> Any: ...
