from typing import Any, Optional

LOG: Any

class Animation:
    fps: Any = ...
    frames_per_loop: Any = ...
    actors: Any = ...
    _precomputed_polydatas: Any = ...
    _current_frame: int = ...
    def __init__(self, loop_duration: Any, fps: int = ...) -> None: ...
    def _add_actor(self, mesh: Any, faces_motion: Optional[Any] = ..., faces_colors: Optional[Any] = ..., edges: bool = ...): ...
    def add_body(self, body: Any, faces_motion: Optional[Any] = ..., faces_colors: Optional[Any] = ..., edges: bool = ...): ...
    def add_free_surface(self, free_surface: Any, faces_elevation: Any): ...
    def _callback(self, renderer: Any, event: Any) -> None: ...
    def run(self, camera_position: Any = ..., resolution: Any = ...) -> None: ...
    def save(self, filepath: Any, nb_loops: int = ..., camera_position: Any = ..., resolution: Any = ...) -> None: ...
