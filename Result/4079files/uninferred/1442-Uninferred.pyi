import sqlite3
import uuid
from typing import Any

class SQLiteDB(sqlite3.Connection):
    __slots__: Any = ...
    query: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def cursor(self): ...

class NamesDB:
    __slots__: Any = ...
    _db: Any = ...
    def __init__(self, data_path: str) -> None: ...
    def submit(version: int, names: Any) -> Any: ...
    def retrieve(version: int, keys: Any) -> Any: ...
    inst_id: Any = ...
    def query_instid() -> uuid.UUID: ...
    def close(self) -> None: ...
