import abc
from abc import ABC, abstractmethod
from mathutils import Vector as Vector
from typing import Any

SCALE_FACTOR: float
ROTATION_VEC: Any
ORIGINAL_ROTATION_VEC: Any
DIST_LIM: float
TARGET_SPEED: float

class Object(ABC, metaclass=abc.ABCMeta):
    sierpinski_scale: Any = ...
    loc: Any = ...
    radius: Any = ...
    name: Any = ...
    verts: Any = ...
    edges: Any = ...
    faces: Any = ...
    mesh_data: Any = ...
    obj: Any = ...
    def __init__(self, radius: float, location: tuple, name: str) -> None: ...
    def _init_mesh(self) -> None: ...
    def _init_obj(self, link: bool = ...) -> None: ...
    @staticmethod
    def scale_objects(object: dict, grid_val: Any, scale_factor: Any=...) -> Any: ...
    @staticmethod
    def rotate_objects(object: dict, grid_val: Any, rotation_vec: Any=..., original_rot_vec: Any=...) -> Any: ...
    @classmethod
    def obj_replication(cls: Any, obj: dict, max_depth: int) -> Any: ...
    @classmethod
    @abstractmethod
    def replicate_shrink_step(cls: Any, obj: dict, max_depth: int) -> Any: ...

class Cube(Object):
    sierpinski_scale: Any = ...
    verts: Any = ...
    faces: Any = ...
    def __init__(self, radius: float, location: tuple) -> None: ...
    @classmethod
    def replicate_shrink_step(cls: Any, cube: dict, max_depth: int) -> Any: ...

class Pyramid(Object):
    sierpinski_scale: Any = ...
    verts: Any = ...
    faces: Any = ...
    def __init__(self, radius: float, location: tuple) -> None: ...
    @classmethod
    def replicate_shrink_step(cls: Any, pyramid: dict, depth: int) -> Any: ...

def update_grid(objs: Any, target: Any) -> None: ...
def move_target(target: Any) -> None: ...
def frame_handler(scene: Any, objs: Any, target: Any, num_frames_change: Any) -> None: ...
def main(_: Any): ...