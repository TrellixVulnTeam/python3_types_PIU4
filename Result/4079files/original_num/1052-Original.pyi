# (generated with --quick)

import io
from typing import Any, Callable, Coroutine, Dict, List, Optional, Tuple, Type, TypeVar, Union

Database: Any
StringIO: Type[io.StringIO]
_csv: module
aiofiles: Any
csv: module

_TReader = TypeVar('_TReader', bound=Reader)

class Get_Reader:
    fh: Any
    file_or_name: Any
    is_file: bool
    is_io: bool
    reader_kwargs: Dict[nothing, nothing]
    def __aenter__(self) -> Coroutine[Any, Any, Union[Reader, _csv._reader]]: ...
    def __aexit__(self, exc_type, exc, tb) -> Coroutine[Any, Any, None]: ...
    def __init__(self, file_or_name, **reader_kwargs) -> None: ...

class Loader(_CSVReader):
    __doc__: str
    converter: Any
    database: Any
    db_table: Any
    field_names: Any
    fields: Any
    file_or_name: Any
    filename: Any
    has_header: Any
    model: Any
    reader_kwargs: Dict[str, Any]
    sample_size: Any
    def __init__(self, db_or_model, file_or_name, fields = ..., field_names = ..., has_header = ..., sample_size = ..., converter = ..., db_table = ..., pk_in_csv = ..., **reader_kwargs) -> None: ...
    def analyze_csv(self) -> None: ...
    def clean_field_name(self, s) -> Any: ...
    def get_converter(self) -> Any: ...
    def get_model_class(self, field_names, fields) -> Any: ...
    def load(self) -> coroutine: ...

class Reader:
    delimiter: Any
    fh: Any
    kws: Dict[nothing, nothing]
    def __aiter__(self: _TReader) -> _TReader: ...
    def __anext__(self) -> coroutine: ...
    def __init__(self, fh, delimiter = ..., **kws) -> None: ...

class RowConverter(_CSVReader):
    __doc__: str
    database: Any
    date_formats: List[str]
    datetime_formats: List[str]
    has_header: Any
    sample_size: Any
    def __init__(self, database, has_header = ..., sample_size = ...) -> None: ...
    def analyze(self, rows) -> list: ...
    def default(self, value) -> bool: ...
    def extract_rows(self, file_or_name, **reader_kwargs) -> Coroutine[Any, Any, Tuple[Any, list]]: ...
    def get_checks(self) -> List[Callable[[Any], Any]]: ...
    def is_date(self, value) -> Optional[bool]: ...
    def is_datetime(self, value) -> Optional[bool]: ...
    def is_float(self, value) -> Optional[bool]: ...
    def is_integer(self, value) -> Any: ...
    def matches_date(self, value, formats) -> Optional[bool]: ...

class _CSVReader:
    def get_reader(self, file_or_name, **reader_kwargs) -> Get_Reader: ...

def __getattr__(name) -> Any: ...
def aioload_csv(db_or_model, file_or_name, fields = ..., field_names = ..., has_header = ..., sample_size = ..., converter = ..., db_table = ..., pk_in_csv = ..., **reader_kwargs) -> coroutine: ...
def convert_field(field_class, **field_kwargs) -> Callable[[Any], Any]: ...
