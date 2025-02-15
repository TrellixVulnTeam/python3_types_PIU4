import logging
from typing import Any, Optional

def get_args_parser(): ...

LOG_LEVELS: Any

class _ParentLogHandler(logging.Handler):
    parent: Any = ...
    def __init__(self, parent: Any, level: Any = ...) -> None: ...
    def emit(self, record: Any) -> None: ...

def init_logger(args: Any, parent: Optional[Any] = ..., fmt: Optional[Any] = ...): ...
def parse_args(argv: Optional[Any] = ...): ...
def get_arg(args: Any, config: Any, name: Any, section: Any, default: Any, cast: Any): ...
