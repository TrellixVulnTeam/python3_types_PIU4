from pyignite.datatypes.prop_codes import *
from typing import Any

def test_cache_create(client: Any) -> None: ...
def test_cache_remove(client: Any) -> None: ...
def test_cache_get(client: Any) -> None: ...
def test_cache_config(client: Any) -> None: ...
def test_cache_get_put(client: Any) -> None: ...
def test_cache_binary_get_put(client: Any) -> None: ...
def test_get_binary_type(client: Any) -> None: ...
def test_cache_scan(client: Any, page_size: Any) -> None: ...
def test_get_and_put_if_absent(client: Any) -> None: ...