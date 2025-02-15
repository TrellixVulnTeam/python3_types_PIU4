# (generated with --quick)

import typing
from typing import Any, Dict, List, Optional, Pattern, Sequence, Tuple, Type, TypeVar, Union

Counter: Type[typing.Counter]
Image: module
ImgurClient: Any
config: Any
re: module

_T = TypeVar('_T')

class Goban:
    Group: Type[List[Move]]
    captures: Dict[Any, int]
    history: List[dict]
    image_url: Any
    imgur_client: Any
    moves: Any
    next_turn_color: Any
    passed: bool
    votes: dict
    def __init__(self) -> None: ...
    def _toggle_color(self) -> str: ...
    def build_group(self, move, group = ...) -> Any: ...
    def current_game_state(self) -> Dict[Union[str, Tuple[int, int]], Optional[str]]: ...
    def draw_board(self, highlighted_move) -> None: ...
    def get_adjacent_moves(self, move) -> List[Move]: ...
    def get_captures(self) -> str: ...
    def get_liberties(self, group) -> int: ...
    def get_votes(self) -> str: ...
    def is_valid(self, move) -> bool: ...
    def pass_move(self) -> str: ...
    def place_stone(self, move) -> None: ...
    def play_move(self) -> Optional[str]: ...
    def remove_if_captured(self, move) -> None: ...
    def resign(self) -> str: ...
    def restart_game(self) -> None: ...
    def show_board(self) -> Any: ...
    def superko(self, move) -> bool: ...
    def vote_move(self, move, user) -> str: ...
    def vote_random(self, user, hidden) -> str: ...

class Move:
    MOVE_PATTERN: Pattern[str]
    coordinates: Optional[Tuple[int, int]]
    hidden: Any
    move_reference: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, move_reference, hidden = ...) -> None: ...
    def __str__(self) -> str: ...
    @classmethod
    def from_coordinates(cls, x, y, hidden = ...) -> Any: ...

def choice(seq: Sequence[_T]) -> _T: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def randrange(start: int, stop: Optional[int] = ..., step: int = ...) -> int: ...
