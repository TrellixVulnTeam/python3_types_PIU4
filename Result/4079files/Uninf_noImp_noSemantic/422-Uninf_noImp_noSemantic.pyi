from TFCommon.Initializer import random_orthogonal_initializer as random_orthogonal_initializer
from typing import Any, Optional

class Maxout:
    _units: Any = ...
    def __init__(self, units: Any) -> None: ...
    @property
    def units(self): ...
    def __call__(self, x: Any, scope: Optional[Any] = ...): ...