from pyglet.gl import *
import esper
import pyglet
from typing import Any, Optional

FPS: int
RESOLUTION: Any
BGCOLOR: Any

class Velocity:
    x: Any = ...
    y: Any = ...
    def __init__(self, x: float = ..., y: float = ...) -> None: ...

class Renderable:
    texture: Any = ...
    _x: Any = ...
    _y: Any = ...
    w: Any = ...
    h: Any = ...
    group: Any = ...
    vertex_list: Any = ...
    _dirty: bool = ...
    def __init__(self, texture: Any, width: Any, height: Any, posx: Any, posy: Any) -> None: ...
    @property
    def x(self): ...
    @x.setter
    def x(self, val: Any) -> None: ...
    @property
    def y(self): ...
    @y.setter
    def y(self, val: Any) -> None: ...

class MovementProcessor(esper.Processor):
    minx: Any = ...
    miny: Any = ...
    maxx: Any = ...
    maxy: Any = ...
    def __init__(self, minx: Any, miny: Any, maxx: Any, maxy: Any) -> None: ...
    def process(self) -> None: ...

class TextureRenderProcessor(esper.Processor):
    batch: Any = ...
    def __init__(self, batch: Any) -> None: ...
    def process(self) -> None: ...
    def draw_texture(self, renderable: Any) -> None: ...

def texture_from_image(image_name: Any): ...

class TextureEnableGroup(pyglet.graphics.Group):
    def set_state(self) -> None: ...
    def unset_state(self) -> None: ...

texture_enable_group: Any

class TextureBindGroup(pyglet.graphics.Group):
    texture: Any = ...
    blend_src: Any = ...
    blend_dest: Any = ...
    def __init__(self, texture: Any) -> None: ...
    def set_state(self) -> None: ...
    def unset_state(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

def run(args: Optional[Any] = ...) -> None: ...