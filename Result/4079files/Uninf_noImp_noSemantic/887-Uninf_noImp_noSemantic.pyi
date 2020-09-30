import logging
import unittest
from typing import Any, Optional

class FailedToRaise(Exception): ...

class AssertRaises:
    expected: Any = ...
    def __init__(self, exc: Any) -> None: ...
    def __enter__(self): ...
    exception: Any = ...
    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any): ...

class CompatTestCase(unittest.TestCase):
    def assertIsNotNone(self, value: Any, *args: Any) -> None: ...
    def assertIsNone(self, value: Any, *args: Any) -> None: ...
    def assertRaises(self, excClass: Any, callableObj: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
    def assertIsInstance(self, obj: Any, cls: Any, msg: Optional[Any] = ...) -> None: ...
    def assertDictEqual(self, d1: Any, d2: Any, msg: Optional[Any] = ...) -> None: ...
    def assertListEqual(self, list1: Any, list2: Any, msg: Optional[Any] = ...) -> None: ...

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

def getmembers_issubclass(object: Any, classinfo: Any): ...