import numpy
import typing
from .encoder_base import EncoderBase
from typing import Any

class ITQEncoder(EncoderBase):
    class TrainedITQEncoder:
        def __init__(self, R: Any, pca: Any, bits: Any) -> None: ...
        def encode(self, vector: Any): ...
        def encode_multi(self, data_matrix: Any): ...
    iteration: Any = ...
    num_bit: Any = ...
    trained_encoder: Any = ...
    def __init__(self, iteration: int=..., num_bit: int=...) -> None: ...
    def __preprocess(self, data: Any, bits: Any): ...
    def __fit(self, data: Any, bits: Any, iteration: Any): ...
    def fit(self, x_train: numpy.array) -> None: ...
    def transform_generator(self, x_test: typing.Iterable[typing.Iterator[float]]) -> Any: ...
    def inverse_transform_generator(self, x_test: typing.Iterable[typing.Iterator[int]]) -> Any: ...