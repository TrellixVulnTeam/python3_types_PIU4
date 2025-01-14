import loopy.target.numba as base_numba
from typing import Any

LOG: Any

class NumbaTarget(base_numba.NumbaTarget):
    no_jit: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_kernel_executor_cache_key(self, *args: Any, **kwargs: Any): ...
    def get_kernel_executor(self, knl: Any, *args: Any, **kwargs: Any): ...

class NumbaCudaTarget(base_numba.NumbaCudaTarget):
    def get_kernel_executor_cache_key(self, *args: Any, **kwargs: Any): ...
    def get_kernel_executor(self, knl: Any, *args: Any, **kwargs: Any): ...
    def _wrap_dims(self, nbc_knl: Any): ...
