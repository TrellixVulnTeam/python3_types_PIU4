import unittest

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_1(self) -> None: ...
    def test_2(self) -> None: ...
    def test_3(self) -> None: ...
