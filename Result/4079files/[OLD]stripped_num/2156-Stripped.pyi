# (generated with --quick)

from typing import Any, Generator, Tuple

logging: module
os: module
subprocess: module
sys: module
time: module

def build_image(repo_path, repo_name) -> None: ...
def get_sys_args() -> Tuple[Any, Any]: ...
def init_logger() -> None: ...
def run_cmd(args, timeout = ..., **kwargs) -> int: ...
def yield_dockerfiles(repo_path, repo_name, absolute = ...) -> Generator[Tuple[str, Any], Any, None]: ...
