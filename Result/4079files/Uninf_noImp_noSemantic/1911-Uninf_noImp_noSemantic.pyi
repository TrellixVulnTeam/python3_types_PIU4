import unittest
from typing import Any, BinaryIO, Sequence, Tuple

def make_plaintexts(streams: Sequence[BinaryIO], num_bytes: Any=...) -> Tuple[Tuple[int, ...]]: ...
def make_keys(streams: Sequence[BinaryIO], necessary_nibble_grams: Tuple[Tuple[int, ...]]) -> Any: ...
def make_credentials(num_secrets: Any, num_bytes: Any=...) -> Tuple[Tuple[str, ...], Tuple[str, ...]]: ...

class TestMain(unittest.TestCase):
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_entropy_test(self) -> None: ...
    def test_crypto(self) -> None: ...
