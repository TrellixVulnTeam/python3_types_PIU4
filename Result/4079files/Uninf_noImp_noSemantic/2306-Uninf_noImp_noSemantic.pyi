import enum
from . import SceneNode
from UM.Math.Matrix import Matrix
from UM.Math.Ray import Ray
from UM.Math.Vector import Vector
from UM.Mesh.MeshData import MeshData as MeshData
from typing import Any, Dict, Optional, Tuple

class Camera(SceneNode.SceneNode):
    class PerspectiveMode(enum.Enum):
        PERSPECTIVE: str = ...
        ORTHOGRAPHIC: str = ...
    @staticmethod
    def getDefaultZoomFactor(): ...
    _name: Any = ...
    _projection_matrix: Any = ...
    _perspective: bool = ...
    _viewport_width: int = ...
    _viewport_height: int = ...
    _window_width: int = ...
    _window_height: int = ...
    _auto_adjust_view_port_size: bool = ...
    _cached_view_projection_matrix: Any = ...
    _zoom_factor: Any = ...
    def __init__(self, name: str=..., parent: SceneNode.SceneNode=...) -> None: ...
    def __deepcopy__(self, memo: Dict[int, object]) -> Camera: ...
    def getZoomFactor(self): ...
    def setZoomFactor(self, zoom_factor: float) -> None: ...
    def setMeshData(self, mesh_data: Optional[MeshData]) -> None: ...
    def getAutoAdjustViewPort(self) -> bool: ...
    def setAutoAdjustViewPort(self, auto_adjust: bool) -> None: ...
    def getProjectionMatrix(self) -> Matrix: ...
    def getViewportWidth(self) -> int: ...
    def setViewportWidth(self, width: int) -> None: ...
    def setViewportHeight(self, height: int) -> None: ...
    def setViewportSize(self, width: int, height: int) -> None: ...
    def _updatePerspectiveMatrix(self) -> None: ...
    def getViewProjectionMatrix(self): ...
    def _updateWorldTransformation(self) -> None: ...
    def getViewportHeight(self) -> int: ...
    def setWindowSize(self, width: int, height: int) -> None: ...
    def getWindowSize(self) -> Tuple[int, int]: ...
    def render(self, renderer: Any) -> bool: ...
    def setProjectionMatrix(self, matrix: Matrix) -> None: ...
    def isPerspective(self) -> bool: ...
    def setPerspective(self, perspective: bool) -> None: ...
    perspectiveChanged: Any = ...
    def getRay(self, x: float, y: float) -> Ray: ...
    def project(self, position: Vector) -> Tuple[float, float]: ...
    def _preferencesChanged(self, key: Any) -> None: ...
