import pyopencl as cl
from typing import Iterator, List

def get_default_device(use_gpu: bool=...) -> cl.Device: ...
def get_devices_by_name(name: str, case_sensitive: bool=...) -> List[cl.Device]: ...
def range_bitwise_shift(low: int, high: int, n: int) -> Iterator[int]: ...
