import cozmo
from cozmo.objects import CustomObject as CustomObject, CustomObjectMarkers as CustomObjectMarkers, CustomObjectTypes as CustomObjectTypes
from typing import Any

CYAN: Any
PINK: Any
YELLOW: Any
GREEN: Any
RED: Any
BLUE: Any
WHITE: Any
OFF: Any

class VisionCube(cozmo.objects.LightCube):
    _chaser: Any = ...
    _cube: Any = ...
    _color: Any = ...
    def __init__(self, *a: Any, **kw: Any) -> None: ...
    def color(self): ...
    def set_color(self, value: cozmo.lights.Color) -> Any: ...
    def start_light_chaser(self, value: cozmo.lights.Color) -> Any: ...
    def rainbow_chaser(self) -> None: ...
    def stop_light_chaser(self) -> None: ...
    def turn_of_lights(self) -> None: ...
