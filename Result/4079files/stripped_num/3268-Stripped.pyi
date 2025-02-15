# (generated with --quick)

from typing import Any, Optional, TypeVar, Union

os: module
shutil: module

AnyStr = TypeVar('AnyStr', str, bytes)

def abspath(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def ensure_exists(fpath) -> None: ...
def exists(path: Union[_PathLike, bytes, int, str]) -> bool: ...
def isdir(path: Union[_PathLike, bytes, str]) -> bool: ...
def isfile(path: Union[_PathLike, bytes, str]) -> bool: ...
def makedirs(name: Union[_PathLike, bytes, str], mode: int = ..., exist_ok: bool = ...) -> None: ...
def mknod(path: Union[_PathLike, bytes, str], mode: int = ..., device: int = ..., *, dir_fd: Optional[int] = ...) -> None: ...
def realpath(filename: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def require_exists(fpath) -> None: ...
def up_by_n_dirs(path, n) -> Any: ...
def validate_executables(xs) -> None: ...
def vimdir_path(*components) -> Any: ...
