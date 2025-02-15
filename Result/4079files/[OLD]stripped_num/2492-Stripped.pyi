# (generated with --quick)

import contextlib
import hashlib
from typing import Any, Callable, Iterator, Optional, TypeVar, Union
import unittest.case

gzip_cache: module
os: module
tempfile: module
temporary_folder: Callable[..., contextlib._GeneratorContextManager]
time: module
unittest: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T = TypeVar('_T')

class TestGzipCache(unittest.case.TestCase):
    def test_creates_gzip_file(self) -> None: ...
    def test_creates_same_gzip_file(self) -> None: ...
    def test_overwrites_gzip_file(self) -> None: ...
    def test_should_compress(self) -> None: ...
    def test_should_overwrite(self) -> None: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def get_md5(filepath) -> str: ...
def md5(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
def mkdtemp(suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ...) -> AnyStr: ...
def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
