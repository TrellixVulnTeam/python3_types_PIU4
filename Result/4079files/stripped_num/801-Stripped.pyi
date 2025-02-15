# (generated with --quick)

from typing import Any, Dict, Type

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
    path: Any
    sets: Dict[Any, SkDataSet]
    def __del__(self) -> None: ...
    def __getitem__(self, item) -> SkDataSet: ...
    def __init__(self, file_path) -> None: ...
    def import_from(self, source, dset_id = ..., index_col = ..., target_col = ...) -> None: ...
    def load(self, file_path) -> None: ...

class SkDataColumn:
    column_name: Any
    parent: Any
    def __init__(self, parent, column_name) -> None: ...
    def categorize(self, categories = ..., max_categories = ...) -> None: ...
    def replace(self, dict_map) -> None: ...

class SkDataSet:
    iid: Any
    parent: Any
    result: Any
    steps: Any
    def __getitem__(self, item) -> SkDataColumn: ...
    def __init__(self, parent, iid) -> None: ...
    def attr_dump(self, attr, value) -> None: ...
    def attr_load(self, attr, default = ...) -> Any: ...
    def attr_update(self, attr, value) -> None: ...
    def attrs(self, key, value = ...) -> Any: ...
    def compute(self) -> Any: ...
    def drop_columns(self, max_na_values = ..., max_unique_values = ...) -> None: ...
    def dropna(self) -> None: ...
    def log(self, message) -> None: ...
    def summary(self, compute = ...) -> Any: ...

def cross_fields(data, y, xs, bins) -> Any: ...
def pandas_dtype_to_hdf5(d) -> Any: ...
def summary(data) -> Any: ...
