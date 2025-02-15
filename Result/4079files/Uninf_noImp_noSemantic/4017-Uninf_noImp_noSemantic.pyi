from typing import Any

DOCKER_REGISTRY: Any
DEFAULT_TIMEOUT: Any
_error_counter: int

def find_repo_path(base: str) -> str: ...
def get_sys_args() -> tuple: ...
def get_image_url(repo_name: str, short_name: str=..., absolute: bool=...) -> str: ...
def yield_dockerfiles(repo_path: str, repo_name: str, absolute: bool=...) -> Any: ...
def read_config(path: str=...) -> dict: ...
def run_cmd(args: list, timeout: int=..., **kwargs: Any) -> int: ...
def init_logger() -> None: ...
def counted_error(*args: Any, **kwargs: Any) -> None: ...
def at_exit() -> None: ...
