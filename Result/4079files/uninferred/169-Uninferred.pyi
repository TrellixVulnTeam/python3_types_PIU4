import unittest
from manticore.core import state as state
from manticore.core.smtlib import Operators as Operators
from typing import Any

class EVMTest_GAS(unittest.TestCase):
    _multiprocess_can_split_: bool = ...
    maxDiff: Any = ...
    def _execute(self, new_vm: Any): ...
    def test_GAS_1(self) -> None: ...
