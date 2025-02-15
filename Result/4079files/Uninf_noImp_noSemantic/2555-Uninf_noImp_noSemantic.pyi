from typing import Any, Dict, Iterable, List, Optional, Union

__version__: str
Body = Union[bytes, str]
Stats = Dict[str, Union[str, int]]
DEFAULT_TUBE: str
DEFAULT_PRIORITY: Any
DEFAULT_DELAY: int
DEFAULT_TTR: int

class Job:
    __slots__: Any = ...
    id: Any = ...
    body: Any = ...
    def __init__(self, id: int, body: Body) -> None: ...
JobOrID = Union[Job, int]

class Error(Exception): ...

class UnknownResponseError(Error):
    status: Any = ...
    values: Any = ...
    def __init__(self, status: bytes, values: List[bytes]) -> None: ...

class BeanstalkdError(Error): ...
class BadFormatError(BeanstalkdError): ...

class BuriedError(BeanstalkdError):
    id: Any = ...
    def __init__(self, values: List[bytes]=...) -> None: ...

class DeadlineSoonError(BeanstalkdError): ...
class DrainingError(BeanstalkdError): ...
class ExpectedCrlfError(BeanstalkdError): ...
class InternalError(BeanstalkdError): ...
class JobTooBigError(BeanstalkdError): ...
class NotFoundError(BeanstalkdError): ...
class NotIgnoredError(BeanstalkdError): ...
class OutOfMemoryError(BeanstalkdError): ...
class TimedOutError(BeanstalkdError): ...
class UnknownCommandError(BeanstalkdError): ...

ERROR_RESPONSES: Any

class Client:
    _sock: Any = ...
    _reader: Any = ...
    encoding: Any = ...
    def __init__(self, host: str=..., port: int=..., encoding: Optional[str]=..., use: str=..., watch: Union[str, Iterable[str]]=...) -> None: ...
    def __enter__(self) -> Client: ...
    def __exit__(self, *args: Any) -> None: ...
    def close(self) -> None: ...
    def _send_cmd(self, cmd: bytes, expected: bytes) -> List[bytes]: ...
    def _read_chunk(self, size: int) -> bytes: ...
    def _int_cmd(self, cmd: bytes, expected: bytes) -> int: ...
    def _job_cmd(self, cmd: bytes, expected: bytes) -> Job: ...
    def _peek_cmd(self, cmd: bytes) -> Job: ...
    def _stats_cmd(self, cmd: bytes) -> Stats: ...
    def _list_cmd(self, cmd: bytes) -> List[str]: ...
    def put(self, body: Body, priority: int=..., delay: int=..., ttr: int=...) -> int: ...
    def use(self, tube: str) -> None: ...
    def reserve(self, timeout: Optional[int]=...) -> Job: ...
    def delete(self, job: JobOrID) -> None: ...
    def release(self, job: Job, priority: int=..., delay: int=...) -> None: ...
    def bury(self, job: Job, priority: int=...) -> None: ...
    def touch(self, job: Job) -> None: ...
    def watch(self, tube: str) -> int: ...
    def ignore(self, tube: str) -> int: ...
    def peek(self, id: int) -> Job: ...
    def peek_ready(self) -> Job: ...
    def peek_delayed(self) -> Job: ...
    def peek_buried(self) -> Job: ...
    def kick(self, bound: int) -> int: ...
    def kick_job(self, job: JobOrID) -> None: ...
    def stats_job(self, job: JobOrID) -> Stats: ...
    def stats_tube(self, tube: str) -> Stats: ...
    def stats(self) -> Stats: ...
    def tubes(self) -> List[str]: ...
    def using(self) -> str: ...
    def watching(self) -> List[str]: ...
    def pause_tube(self, tube: str, delay: int) -> None: ...

def _to_id(j: JobOrID) -> int: ...
def _parse_response(line: bytes, expected: bytes) -> List[bytes]: ...
def _parse_chunk(data: bytes, size: int) -> bytes: ...
def _parse_simple_yaml(buf: bytes) -> Stats: ...
def _parse_simple_yaml_list(buf: bytes) -> List[str]: ...
