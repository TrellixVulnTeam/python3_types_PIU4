# (generated with --quick)

from typing import Any, Generator, NoReturn, Tuple, TypeVar, Union

DEFAULT_TIMEOUT: int
DOCKER_REGISTRY: str
_error_counter: int
glob: module
logging: module
os: module
posixpath: module
subprocess: module
sys: module
yaml: module

_T0 = TypeVar('_T0')

def at_exit() -> NoReturn: ...
def counted_error(*args, **kwargs) -> None: ...
def find_repo_path(base: _T0) -> Union[str, _T0]: ...
def get_image_url(repo_name: _T0, short_name = ..., absolute = ...) -> Union[str, _T0]: ...
def get_sys_args() -> Tuple[str, str]: ...
def init_logger() -> None: ...
def read_config(path = ...) -> Any: ...
def run_cmd(args, timeout = ..., **kwargs) -> int: ...
def yield_dockerfiles(repo_path, repo_name, absolute = ...) -> Generator[Tuple[str, str], Any, None]: ...
