from typing import Any

class MockConnection:
    h: Any = ...
    u: Any = ...
    k: Any = ...
    failure: Any = ...
    access_count: int = ...
    def __init__(self, h: Any, u: Any, k: Any, failure: bool = ...) -> None: ...
    def open_session(self): ...
    def is_active(self): ...
    def is_authenticated(self): ...

def test_hostsession_enter(monkeypatch: Any): ...
def test_hostsession_enter_fail(monkeypatch: Any): ...
def test_connection_cache(): ...
def test_connection_cache_none(): ...
