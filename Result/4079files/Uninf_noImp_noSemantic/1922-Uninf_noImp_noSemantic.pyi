import unittest
from typing import Any

class TestAutoAssignments(unittest.TestCase):
    protocol: Any = ...
    decodings: Any = ...
    def setUp(self) -> None: ...
    def test_message_type_assign_by_value(self) -> None: ...
    def test_two_assign_participants_by_rssi(self) -> None: ...
