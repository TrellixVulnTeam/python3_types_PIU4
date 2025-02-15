import abc
from abc import ABC, abstractmethod
from typing import Any

class AImageModel(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def model(self) -> Any: ...
    def process_input(self, image_batch: Any) -> None: ...

class VGGImageModel(AImageModel):
    _model: Any = ...
    _vgg_features: Any = ...
    _id_map: Any = ...
    def __init__(self, data_root: Any) -> None: ...
    def model(self): ...
    def process_input(self, image_batch: Any): ...
