# (generated with --quick)

from typing import Any

SQLiteStorage: Any
os: module
pytest: Any
storage: Any
test_ttl_lte0: Any
time: module

def ensure_index(db, table_name, columns, unique) -> None: ...
def test_clear(storage) -> None: ...
def test_items(storage) -> None: ...
def test_maxsize(tmpdir) -> None: ...
def test_remove(tmpdir) -> None: ...
def test_repr(tmpdir) -> None: ...
def test_schema_fifo() -> None: ...
def test_schema_lfu() -> None: ...
def test_schema_lru() -> None: ...
def test_set_get(storage) -> None: ...
def test_ttl_gt0(tmpdir) -> None: ...
