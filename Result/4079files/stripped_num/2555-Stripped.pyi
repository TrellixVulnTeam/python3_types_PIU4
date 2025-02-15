# (generated with --quick)

from typing import Any, BinaryIO, Dict, List, Optional, Type, TypeVar, Union

Stats = Dict[str, Union[int, str]]

Body: Type[Union[bytes, str]]
DEFAULT_DELAY: int
DEFAULT_PRIORITY: int
DEFAULT_TTR: int
DEFAULT_TUBE: str
ERROR_RESPONSES: Dict[bytes, type]
JobOrID: Type[Union[Job, int]]
__version__: str
socket: module

_TClient = TypeVar('_TClient', bound=Client)

class BadFormatError(BeanstalkdError):
    __doc__: str

class BeanstalkdError(Error):
    __doc__: str

class BuriedError(BeanstalkdError):
    __doc__: str
    id: Optional[int]
    def __init__(self, values = ...) -> None: ...

class Client:
    __doc__: str
    _reader: BinaryIO
    _sock: socket.socket
    encoding: Any
    def __enter__(self: _TClient) -> _TClient: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, host = ..., port = ..., encoding = ..., use = ..., watch = ...) -> None: ...
    def _int_cmd(self, cmd, expected) -> int: ...
    def _job_cmd(self, cmd, expected) -> Job: ...
    def _list_cmd(self, cmd) -> list: ...
    def _peek_cmd(self, cmd) -> Job: ...
    def _read_chunk(self, size) -> bytes: ...
    def _send_cmd(self, cmd, expected) -> List[bytes]: ...
    def _stats_cmd(self, cmd) -> dict: ...
    def bury(self, job, priority = ...) -> None: ...
    def close(self) -> None: ...
    def delete(self, job) -> None: ...
    def ignore(self, tube) -> int: ...
    def kick(self, bound) -> int: ...
    def kick_job(self, job) -> None: ...
    def pause_tube(self, tube, delay) -> None: ...
    def peek(self, id) -> Any: ...
    def peek_buried(self) -> Any: ...
    def peek_delayed(self) -> Any: ...
    def peek_ready(self) -> Any: ...
    def put(self, body, priority = ..., delay = ..., ttr = ...) -> int: ...
    def release(self, job, priority = ..., delay = ...) -> None: ...
    def reserve(self, timeout = ...) -> Job: ...
    def stats(self) -> Any: ...
    def stats_job(self, job) -> Any: ...
    def stats_tube(self, tube) -> Any: ...
    def touch(self, job) -> None: ...
    def tubes(self) -> Any: ...
    def use(self, tube) -> None: ...
    def using(self) -> Any: ...
    def watch(self, tube) -> int: ...
    def watching(self) -> Any: ...

class DeadlineSoonError(BeanstalkdError):
    __doc__: str

class DrainingError(BeanstalkdError):
    __doc__: str

class Error(Exception):
    __doc__: str

class ExpectedCrlfError(BeanstalkdError):
    __doc__: str

class InternalError(BeanstalkdError):
    __doc__: str

class Job:
    __slots__ = ["body", "id"]
    __doc__: str
    body: Any
    id: Any
    def __init__(self, id, body) -> None: ...

class JobTooBigError(BeanstalkdError):
    __doc__: str

class NotFoundError(BeanstalkdError):
    __doc__: str

class NotIgnoredError(BeanstalkdError):
    __doc__: str

class OutOfMemoryError(BeanstalkdError):
    __doc__: str

class TimedOutError(BeanstalkdError):
    __doc__: str

class UnknownCommandError(BeanstalkdError):
    __doc__: str

class UnknownResponseError(Error):
    __doc__: str
    status: Any
    values: Any
    def __init__(self, status, values) -> None: ...

def _parse_chunk(data, size) -> Any: ...
def _parse_response(line, expected) -> list: ...
def _parse_simple_yaml(buf) -> dict: ...
def _parse_simple_yaml_list(buf) -> list: ...
def _to_id(j) -> Any: ...
