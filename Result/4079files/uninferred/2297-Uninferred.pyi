import moderngl
from demosys.context.base import BaseWindow as BaseWindow
from demosys.scene import Scene as Scene, camera as camera
from rocket.tracks import Track as Track
from typing import Any, Optional, Type, Union

class Effect:
    runnable: bool = ...
    _name: str = ...
    _label: str = ...
    _window: BaseWindow = ...
    _project: demosys.project.base.BaseProject = ...
    _ctx: moderngl.Context = ...
    _sys_camera: camera.SystemCamera = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def post_load(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def label(self) -> str: ...
    @property
    def window(self) -> BaseWindow: ...
    @property
    def ctx(self) -> moderngl.Context: ...
    @property
    def sys_camera(self) -> camera.SystemCamera: ...
    def draw(self, time: float, frametime: float, target: moderngl.Framebuffer) -> Any: ...
    def get_program(self, label: str) -> moderngl.Program: ...
    def get_texture(self, label: str) -> Union[moderngl.Texture, moderngl.TextureArray, moderngl.Texture3D, moderngl.TextureCube]: ...
    def get_track(self, name: str) -> Track: ...
    def get_scene(self, label: str) -> Scene: ...
    def get_data(self, label: str) -> Any: ...
    def get_effect(self, label: str) -> Effect: ...
    def get_effect_class(self, effect_name: str, package_name: str=...) -> Type[Effect]: ...
    def create_projection(self, fov: float=..., near: float=..., far: float=..., aspect_ratio: float=...) -> Any: ...
    def create_transformation(self, rotation: Optional[Any] = ..., translation: Optional[Any] = ...): ...
    def create_normal_matrix(self, modelview: Any): ...
