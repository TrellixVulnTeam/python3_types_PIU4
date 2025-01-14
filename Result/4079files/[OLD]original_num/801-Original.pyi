# (generated with --quick)

from typing import Any, Dict, NoReturn, Optional, Type

StepSkData: Any
datetime: Type[datetime.datetime]
h5py: Any
np: module
odo: Any
os: module
pd: Any
pickle: module

class SkData:
    __doc__: str
    data: Any
    path: str
    sets: Dict[Any, SkDataSet]
    def __del__(self) -> None: ...
    def __getitem__(self, item) -> SkDataSet: ...
    def __init__(self, file_path: str) -> None: ...
    def import_from(self, source: str, dset_id: Optional[str] = ..., index_col: Optional[str] = ..., target_col: Optional[str] = ...) -> None: ...
    def load(self, file_path: str) -> None: ...

class SkDataColumn:
    column_name: Optional[str]
    parent: Optional[SkDataSet]
    def __init__(self, parent: SkDataSet, column_name: str) -> None: ...
    def categorize(self, categories: Optional[dict] = ..., max_categories: float = ...) -> NoReturn: ...
    def replace(self, dict_map: dict) -> NoReturn: ...

class SkDataSet:
    iid: Optional[str]
    parent: Optional[SkData]
    result: Any
    steps: Any
    def __getitem__(self, item) -> SkDataColumn: ...
    def __init__(self, parent: SkData, iid: str) -> None: ...
    def attr_dump(self, attr: str, value: object) -> None: ...
    def attr_load(self, attr: str, default: object = ...) -> Any: ...
    def attr_update(self, attr: str, value: object) -> NoReturn: ...
    def attrs(self, key: str, value: Optional[str] = ...) -> Any: ...
    def compute(self) -> Any: ...
    def drop_columns(self, max_na_values: Optional[int] = ..., max_unique_values: Optional[int] = ...) -> NoReturn: ...
    def dropna(self) -> NoReturn: ...
    def log(self, message: str) -> None: ...
    def summary(self, compute = ...) -> Any: ...

def cross_fields(data, y: str, xs, bins: int) -> Any: ...
def pandas_dtype_to_hdf5(d) -> Any: ...
def summary(data) -> Any: ...
