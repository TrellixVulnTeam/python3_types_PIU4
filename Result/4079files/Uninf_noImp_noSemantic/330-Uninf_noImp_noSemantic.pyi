from typing import Any, Optional

class AbstractSort:
    implements: Any = ...
    def __init__(self, implements: Optional[Any] = ...) -> None: ...
    @property
    def __sortname__(self): ...
    def __str__(self): ...
    def __repr__(self): ...
