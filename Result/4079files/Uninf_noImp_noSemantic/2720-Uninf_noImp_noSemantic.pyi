from typing import Any

def cache(tmpdir: Any, request: Any) -> None: ...
def test_repr() -> None: ...

keys_and_values: Any
test_names: Any

def test_cache_set_get_in_clear_del(cache: Any, key: Any, value: Any) -> None: ...
def test_duplicates(cache: Any) -> None: ...
def test_function_decorator_noargs(cache: Any): ...
def test_function_decorator_with_args(cache: Any): ...
def test_copy(cache: Any): ...
def test_raises_if_closed(cache: Any) -> None: ...
def test_remove(tmpdir: Any, cache: Any) -> None: ...
def test_types(cache: Any): ...
def test_make_key() -> None: ...
def test__type_name(obj: Any, expected: Any) -> None: ...
def test__type_names() -> None: ...
def test__function_name(obj: Any, expected: Any) -> None: ...
def test_fn_not_callable(cache: Any) -> None: ...
def test_items(cache: Any) -> None: ...
def test_lru(tmpdir: Any, storage: Any): ...
def test_lfu(tmpdir: Any, storage: Any): ...
def test_only_on_errors(): ...
