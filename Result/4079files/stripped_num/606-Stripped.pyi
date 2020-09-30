# (generated with --quick)

from typing import Any

DEBUG: bool
GL: Any
GLRenderer: Any
GLWidget: Any
Image: module
Matrix44: Any
global_variables: Any
numpy: module
threading: module
warnings: module

class GLQuadRenderer(Any):
    _GLQuadRenderer__create_histogram: Any
    _GLQuadRenderer__data: Any
    _GLQuadRenderer__data_texture: Any
    _GLQuadRenderer__do_harmonization: bool
    _GLQuadRenderer__image_height: Any
    _GLQuadRenderer__image_loader_thread: threading.Thread
    _GLQuadRenderer__image_width: Any
    _GLQuadRenderer__loaded: bool
    _GLQuadRenderer__new_texture: Any
    _GLQuadRenderer__size: Any
    _GLQuadRenderer__texture: Any
    _GLQuadRenderer__uniform_data_texture: Any
    _GLQuadRenderer__uniform_do_harmonization: Any
    _GLQuadRenderer__uniform_projection: Any
    _GLQuadRenderer__uniform_texture: Any
    _GLQuadRenderer__uniform_world: Any
    _GLQuadRenderer__view_size: Any
    array_buffer: Any
    fragment_shader: Any
    log_scale: Any
    program: Any
    scale: int
    vertex_array: Any
    vertex_shader: Any
    world: Any
    def _GLQuadRenderer__image_loader(self, path) -> None: ...
    def _GLQuadRenderer__load_texture(self) -> None: ...
    def __init__(self, view_size = ..., create_histogram = ..., size = ...) -> None: ...
    def load(self) -> None: ...
    def load_texture(self, path) -> None: ...
    def render(self) -> None: ...
    def resize(self, width, height) -> None: ...
    def update(self) -> None: ...