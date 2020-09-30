from typing import Any

class Model:
    _response: Any = ...
    __model_image: Any = ...
    __online: Any = ...
    __status: Any = ...
    last_update: Any = ...
    username: Any = ...
    autoupdate: Any = ...
    def __init__(self, username: Any, autoupdate: bool = ...) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, value: Any) -> None: ...
    @property
    def online(self): ...
    @online.setter
    def online(self, value: Any) -> None: ...
    @property
    def model_image(self): ...
    @model_image.setter
    def model_image(self, value: Any) -> None: ...
    def update_model_status(self) -> None: ...
    def update_model_image(self) -> None: ...