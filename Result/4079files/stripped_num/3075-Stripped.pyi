# (generated with --quick)

from typing import Any, List, Optional, TypeVar

Serial: Any
datetime: module
logger: logging.Logger
logging: module
threading: module

_TSomfyRTS = TypeVar('_TSomfyRTS', bound=SomfyRTS)

class SomfyRTS:
    __doc__: str
    _check_queue: threading.Event
    _closed: threading.Event
    _command_queue: List[str]
    _interval_timedelta: datetime.timedelta
    _last_command_time: datetime.datetime
    _lock: threading.Lock
    _queue_is_empty: threading.Event
    _ser: Any
    _thread: Optional[threading.Thread]
    _version: Any
    def __enter__(self: _TSomfyRTS) -> _TSomfyRTS: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, port, interval = ..., version = ..., thread = ...) -> None: ...
    def _do_command(self, command, channels) -> None: ...
    def _do_single_command(self, command, channel) -> None: ...
    def _process_command_queue(self) -> bool: ...
    def _thread_process_queue(self) -> None: ...
    def clear_command_queue(self) -> None: ...
    def close(self) -> None: ...
    def down(self, channels) -> None: ...
    def flush_command_queue(self, timeout = ...) -> bool: ...
    def stop(self, channels) -> None: ...
    def up(self, channels) -> None: ...
