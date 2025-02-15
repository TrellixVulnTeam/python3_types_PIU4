# (generated with --quick)

from typing import Any, Tuple, TypeVar

Logger: Any
Matrix: Any
MeshData: Any
Ray: Any
SceneNode: Any
Signal: Any
Vector: Any
enum: module
numpy: module

_TCamera = TypeVar('_TCamera', bound=Camera)

class Camera(Any):
    PerspectiveMode: type
    _auto_adjust_view_port_size: Any
    _cached_view_projection_matrix: Any
    _name: str
    _perspective: Any
    _projection_matrix: Any
    _viewport_height: Any
    _viewport_width: Any
    _window_height: Any
    _window_width: Any
    _zoom_factor: Any
    perspectiveChanged: Any
    def __deepcopy__(self: _TCamera, memo) -> _TCamera: ...
    def __init__(self, name = ..., parent = ...) -> None: ...
    def _preferencesChanged(self, key) -> None: ...
    def _updatePerspectiveMatrix(self) -> None: ...
    def _updateWorldTransformation(self) -> None: ...
    def getAutoAdjustViewPort(self) -> bool: ...
    @staticmethod
    def getDefaultZoomFactor() -> float: ...
    def getProjectionMatrix(self) -> Any: ...
    def getRay(self, x, y) -> Any: ...
    def getViewProjectionMatrix(self) -> Any: ...
    def getViewportHeight(self) -> int: ...
    def getViewportWidth(self) -> int: ...
    def getWindowSize(self) -> Tuple[int, int]: ...
    def getZoomFactor(self) -> float: ...
    def isPerspective(self) -> bool: ...
    def project(self, position) -> Tuple[Any, Any]: ...
    def render(self, renderer) -> bool: ...
    def setAutoAdjustViewPort(self, auto_adjust) -> None: ...
    def setMeshData(self, mesh_data) -> None: ...
    def setPerspective(self, perspective) -> None: ...
    def setProjectionMatrix(self, matrix) -> None: ...
    def setViewportHeight(self, height) -> None: ...
    def setViewportSize(self, width, height) -> None: ...
    def setViewportWidth(self, width) -> None: ...
    def setWindowSize(self, width, height) -> None: ...
    def setZoomFactor(self, zoom_factor) -> None: ...
