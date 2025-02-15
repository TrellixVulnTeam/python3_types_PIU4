from typing import Any, Optional

__all__: Any
_logger: Any

class FlexError(Exception): ...

class FlexReport:
    data: Any = ...
    root: Any = ...
    def __init__(self, token: Optional[Any] = ..., queryId: Optional[Any] = ..., path: Optional[Any] = ...) -> None: ...
    def topics(self): ...
    def extract(self, topic: str, parseNumbers: Any=...) -> list: ...
    def df(self, topic: str, parseNumbers: Any=...) -> Any: ...
    def download(self, token: Any, queryId: Any) -> None: ...
    def load(self, path: Any) -> None: ...
    def save(self, path: Any) -> None: ...
