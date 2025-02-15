# (generated with --quick)

import numpy
from typing import Any, List, Tuple, Type, Union

ArrayType: Any
L: logging.Logger
array: Type[array.array]
butter: Any
lfilter: Any
logging: module
np: module

def add_silence(snd_data: array.array, seconds: int, rate: int) -> Any: ...
def butter_bandpass(cutfreq: Union[List[float], Tuple[float, float]], sampling_frequency: float, order: int = ...) -> Tuple[Any, Any]: ...
def butter_bandpass_filter(data: numpy.ndarray, cutfreq: Union[List[float], Tuple[float, float]], sampling_frequency: float, order: int = ...) -> Any: ...
def is_silent(snd_data: array.array, threshold: int) -> bool: ...
def normalize(snd_data: array.array, absolute_maximum: int) -> Any: ...
def trim(snd_data: array.array, threshold: int) -> Any: ...
