from typing import Any, Optional

class AntGainBase:
    def __init__(self) -> None: ...
    def get_antenna_gain(self, angle: Any) -> None: ...

class AntGainOmni(AntGainBase):
    ant_gain: float = ...
    def __init__(self, ant_gain: Optional[Any] = ...) -> None: ...
    def get_antenna_gain(self, angle: Any): ...

class AntGainBS3GPP25996(AntGainBase):
    theta_3db: float = ...
    Am: float = ...
    ant_gain: Any = ...
    def __init__(self, number_of_sectors: int = ...) -> None: ...
    def get_antenna_gain(self, angle: Any): ...
