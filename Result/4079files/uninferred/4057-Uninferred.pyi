import unittest
from typing import Any

class TestVoteMove(unittest.TestCase):
    goban: Any = ...
    a1_move: Any = ...
    a2_move: Any = ...
    random_move: Any = ...
    def setUp(self) -> None: ...
    def test_vote_succeeds(self) -> None: ...
    def test_invalid_move(self) -> None: ...
    def test_already_voted(self) -> None: ...
    def test_change_vote(self) -> None: ...
    def test_vote_random(self) -> None: ...