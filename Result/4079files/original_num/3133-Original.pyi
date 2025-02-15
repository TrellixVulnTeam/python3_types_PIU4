# (generated with --quick)

import logging
from typing import List, Match, Optional, Pattern, TextIO, TypeVar, Union

LOG: logging.Logger
stdin: TextIO

AnyStr = TypeVar('AnyStr', str, bytes)

def add_test(database: str, code: str, delete = ..., input_file = ..., output_file = ..., inp_suffix: str = ..., cor_suffix: str = ..., **kwargs) -> None: ...
def basename(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def isdir(path: Union[_PathLike, bytes, str]) -> bool: ...
def makedirs(name: Union[_PathLike, bytes, str], mode: int = ..., exist_ok: bool = ...) -> None: ...
def remove(path: Union[_PathLike, bytes, str], *, dir_fd: Optional[int] = ...) -> None: ...
def search(pattern: Union[Pattern[AnyStr], AnyStr], string: AnyStr, flags: int = ...) -> Optional[Match[AnyStr]]: ...
