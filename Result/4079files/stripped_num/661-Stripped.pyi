# (generated with --quick)

import asyncio.futures
import enum
import simulation.django_communicator
import types
from typing import Any, Coroutine, Type

CoroutineType: Type[types.CoroutineType]
DjangoCommunicator: Type[simulation.django_communicator.DjangoCommunicator]
Enum: Type[enum.Enum]
LOGGER: logging.Logger
SECONDS_TILL_CONSIDERED_INACTIVE: int
asyncio: module
codes: Any
logging: module

class ActivityMonitor:
    __doc__: str
    active_users: Any
    django_communicator: Any
    timer: Timer
    def __init__(self, django_communicator) -> None: ...
    def _start_timer(self) -> None: ...
    def _stop_timer(self) -> None: ...
    def change_status_to_stopped(self) -> Coroutine[Any, Any, None]: ...

class StatusOptions(enum.Enum):
    PAUSED: str
    RUNNING: str
    STOPPED: str

class Timer:
    __doc__: str
    _callback: Any
    _task: asyncio.futures.Future
    _timeout: Any
    def __init__(self, timeout, callback) -> None: ...
    def _job(self) -> Coroutine[Any, Any, None]: ...
    def cancel(self) -> None: ...
    def cancelled(self) -> bool: ...
