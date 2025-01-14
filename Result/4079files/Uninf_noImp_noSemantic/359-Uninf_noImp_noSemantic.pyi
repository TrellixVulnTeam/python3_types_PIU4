import unittest
from typing import Any

class TestLogWrapAsync(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    logger: Any = ...
    stream: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_coroutine_async(self) -> None: ...
    def test_coroutine_async_as_argumented(self) -> None: ...
    def test_coroutine_fail(self) -> None: ...
    def test_exceptions_blacklist(self) -> None: ...

class TestAnnotated(unittest.TestCase):
    logger: Any = ...
    stream: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_annotation_args(self) -> None: ...
