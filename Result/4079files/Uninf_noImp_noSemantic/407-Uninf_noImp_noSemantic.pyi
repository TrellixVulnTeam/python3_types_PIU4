from same.data.constants import Colour
from same.views.gui_client import GuiClient
from typing import Any, List

FONT_PATH: str
GAME_OVER_SIZE: int
SCORE_FONT_SIZE: int

class PyGameClient(GuiClient):
    score_board_height: Any = ...
    board_dimensions: Any = ...
    screen: Any = ...
    size: Any = ...
    colours: Any = ...
    num_columns: Any = ...
    num_rows: Any = ...
    def __init__(self, size: int, num_columns: int, num_rows: int, score_board_height: int, colours: ColourScheme) -> None: ...
    def draw_board(self, balls: List[List[Ball]], boxes: List[List[Box]]) -> Any: ...
    def draw_circle(self, position: tuple, colour: Colour) -> Any: ...
    def draw_score_board(self, score: int, highest_score: int, current_move_score: int, moves: int) -> Any: ...
    def game_over(self, score: int, high_score: int) -> Any: ...
    def end_game(self) -> None: ...
    def get_clicked_ball(self): ...
    def get_current_ball(self): ...
    def get_events(self): ...
