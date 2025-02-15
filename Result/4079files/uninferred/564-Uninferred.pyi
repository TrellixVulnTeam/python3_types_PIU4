from typing import Any

class Result:
    ok: Any = ...
    err: Any = ...
    def __init__(self, variant: Any, value: Any) -> None: ...
    def has_ok(self): ...
    def has_err(self): ...
    def map(self, func: Any): ...

def ok(value: Any): ...
def err(value: Any): ...
