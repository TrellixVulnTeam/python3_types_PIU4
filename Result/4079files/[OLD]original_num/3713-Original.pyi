# (generated with --quick)

import datetime
import pathlib
from typing import Any, Dict, Generator, List, Optional, Tuple, Type, TypeVar

PurePosixPath: Type[pathlib.PurePosixPath]
h5py: Any
np: module

_TOCMio = TypeVar('_TOCMio', bound=OCMio)

class OCMio:
    _OCMio__msm_path: Optional[list]
    _OCMio__patched_msm: List[nothing]
    __doc__: str
    band: Optional[str]
    fid: Any
    filename: Any
    def __enter__(self: _TOCMio) -> _TOCMio: ...
    def __exit__(self, exc_type, exc_value, traceback) -> bool: ...
    def __init__(self, ocm_product) -> None: ...
    def __iter__(self) -> Generator[str, Any, None]: ...
    def __repr__(self) -> str: ...
    def close(self) -> None: ...
    def get_attr(self, attr_name) -> Any: ...
    def get_coverage_time(self) -> Tuple[Any, Any]: ...
    def get_delta_time(self) -> dict: ...
    def get_exposure_time(self) -> Any: ...
    def get_gse_stimuli(self) -> dict: ...
    def get_housekeeping_data(self) -> dict: ...
    def get_instrument_settings(self) -> dict: ...
    def get_msm_attr(self, msm_dset, attr_name) -> Any: ...
    def get_msm_data(self, msm_dset, fill_as_nan = ..., frames = ..., columns = ...) -> dict: ...
    def get_processor_version(self) -> Any: ...
    def get_ref_time(self) -> Dict[Any, datetime.datetime]: ...
    def read_direct_msm(self, msm_dset, dest_sel = ..., dest_dtype = ..., fill_as_nan = ...) -> Optional[dict]: ...
    def select(self, ic_id = ..., *, msm_grp = ...) -> int: ...

def band2channel(dict_a, dict_b, mode = ...) -> Any: ...
