from typing import Any

class DB:
    def query(self, sql: Any): ...

class DBMock:
    def query(self, sql: Any): ...

def run(sql: Any, db: '!DB') -> Any: ...
