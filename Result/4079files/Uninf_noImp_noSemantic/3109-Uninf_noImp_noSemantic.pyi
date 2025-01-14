from magnum import *
from magnum import gl, platform, scenegraph, shaders
from magnum.scenegraph.matrix import Object3D
from typing import Any

class CubeDrawable(scenegraph.Drawable3D):
    _mesh: Any = ...
    _shader: Any = ...
    color: Any = ...
    def __init__(self, object: Object3D, drawables: scenegraph.DrawableGroup3D, mesh: gl.Mesh, shader: shaders.Phong, color: Color4) -> None: ...
    def draw(self, transformation_matrix: Matrix4, camera: scenegraph.Camera3D) -> Any: ...

class PrimitivesSceneGraphExample(platform.Application):
    _scene: Any = ...
    _drawables: Any = ...
    _camera: Any = ...
    _cube: Any = ...
    _cube_drawable: Any = ...
    _previous_mouse_position: Any = ...
    def __init__(self) -> None: ...
    def draw_event(self) -> None: ...
    def mouse_release_event(self, event: platform.Application.MouseEvent) -> Any: ...
    def mouse_move_event(self, event: platform.Application.MouseMoveEvent) -> Any: ...
