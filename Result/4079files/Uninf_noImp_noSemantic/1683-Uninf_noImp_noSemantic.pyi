from typing import Any, Optional

class Command:
    cmd: Any = ...
    bufsize: Any = ...
    timeout: Any = ...
    env: Any = ...
    def __init__(self, cmd: Any, bufsize: int = ..., timeout: int = ..., env: Optional[Any] = ...) -> None: ...
