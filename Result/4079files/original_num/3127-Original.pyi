# (generated with --quick)

import collections
from typing import Any, Callable, Dict, Iterable, List, Sized, Tuple, Type, TypeVar, Union

Position = `namedtuple-Position-x-y`
TileSet = `namedtuple-TileSet-image-positions`

DOWN: `namedtuple-Position-x-y`
KEYDOWN: Any
LEFT: `namedtuple-Position-x-y`
RIGHT: `namedtuple-Position-x-y`
Rect: Any
SIZE: int
TILE_IMAGE_FILE: str
TILE_POSITION_FILE: str
UP: `namedtuple-Position-x-y`
display: Any
ghost: Dict[str, Union[str, `namedtuple-Position-x-y`, List[str]]]
image: Any
maze: List[str]
player: Dict[str, Union[str, `namedtuple-Position-x-y`, Dict[int, `namedtuple-Position-x-y`], List[str]]]
pygame: Any
sprites: List[Dict[str, Union[str, `namedtuple-Position-x-y`, Dict[int, `namedtuple-Position-x-y`], List[str]]]]
tile_image: Any
tile_positions: Dict[str, Any]
tiles: `namedtuple-TileSet-image-positions`

_Tnamedtuple-Position-x-y = TypeVar('_Tnamedtuple-Position-x-y', bound=`namedtuple-Position-x-y`)
_Tnamedtuple-TileSet-image-positions = TypeVar('_Tnamedtuple-TileSet-image-positions', bound=`namedtuple-TileSet-image-positions`)

class `namedtuple-Position-x-y`(tuple):
    __slots__ = ["x", "y"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    x: Any
    y: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Position-x-y`], x, y) -> `_Tnamedtuple-Position-x-y`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Position-x-y`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Position-x-y`: ...
    def _replace(self: `_Tnamedtuple-Position-x-y`, **kwds) -> `_Tnamedtuple-Position-x-y`: ...

class `namedtuple-TileSet-image-positions`(tuple):
    __slots__ = ["image", "positions"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    image: Any
    positions: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-TileSet-image-positions`], image, positions) -> `_Tnamedtuple-TileSet-image-positions`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-TileSet-image-positions`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TileSet-image-positions`: ...
    def _replace(self: `_Tnamedtuple-TileSet-image-positions`, **kwds) -> `_Tnamedtuple-TileSet-image-positions`: ...

def create_display(resolution) -> Any: ...
def draw(maze, sprites, display, tiles) -> None: ...
def draw_grid(data, tile_img, tiles) -> Any: ...
def draw_sprite(sprite, img, tiles) -> None: ...
def event_loop(callbacks, delay = ...) -> Any: ...
def exit_game() -> None: ...
def get_tile_rect(position) -> Any: ...
def load_tile_positions(filename) -> Dict[str, Any]: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def wait_for_key(event) -> None: ...
