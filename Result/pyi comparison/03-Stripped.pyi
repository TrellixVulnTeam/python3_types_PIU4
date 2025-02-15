# (generated with --quick)

import pathlib
from typing import Any, List, Type, TypeVar

L1BioRAD: Any
Path: Type[pathlib.Path]
_MSG_ERR_IO_BAND_: str
get_version: Any
h5py: Any
np: module
shutil: module

_TL1Bpatch = TypeVar('_TL1Bpatch', bound=L1Bpatch)

class L1Bpatch:
    _L1Bpatch__patched_msm: List[nothing]
    __doc__: str
    ckd_dir: pathlib.Path
    data_dir: pathlib.Path
    l1b_patched: pathlib.Path
    l1b_product: pathlib.Path
    def __enter__(self: _TL1Bpatch) -> _TL1Bpatch: ...
    def __exit__(self, exc_type, exc_value, traceback) -> bool: ...
    def __init__(self, l1b_product, data_dir = ..., ckd_dir = ...) -> None: ...
    def absrad(self) -> None: ...
    def check(self) -> None: ...
    def close(self) -> None: ...
    def darkflux(self) -> None: ...
    def offset(self) -> None: ...
    def pixel_quality(self, dpqm, threshold = ...) -> None: ...
    def prnu(self) -> None: ...
    def relrad(self) -> None: ...
