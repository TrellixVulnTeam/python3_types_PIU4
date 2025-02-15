# (generated with --quick)

import collections
from typing import Any, Callable, Dict, Iterable, List, Sized, Tuple, Type, TypeVar, Union

ColumnPair = `namedtuple-ColumnPair-from_column-to_column`
ColumnSort = `namedtuple-ColumnSort-table_name-column_name-direction`
QueryArguments = `namedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`
TableJoin = `namedtuple-TableJoin-table_name-column_pairs-outer_join`

BinaryExpression: Any
Column: Any
ComplexFilter: Any
ConfigurationError: Any
DEFAULT_PAGE: int
DEFAULT_PER_PAGE: int
Function: Any
JoinError: Any
MetaData: Any
NotFoundError: Any
SORT_DIRECTIONS: List[str]
SUPPORTED_FUNCS: List[str]
Select: Any
Table: Any
and_: Any
asc: Any
config: configparser.ConfigParser
configparser: module
create_engine: Any
desc: Any
engine: Any
get_column: Any
log: logging.Logger
logging: module
reflection: Any
s: DBService
select: Any
urllib: module

_Tnamedtuple-ColumnPair-from_column-to_column = TypeVar('_Tnamedtuple-ColumnPair-from_column-to_column', bound=`namedtuple-ColumnPair-from_column-to_column`)
_Tnamedtuple-ColumnSort-table_name-column_name-direction = TypeVar('_Tnamedtuple-ColumnSort-table_name-column_name-direction', bound=`namedtuple-ColumnSort-table_name-column_name-direction`)
_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list = TypeVar('_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list', bound=`namedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`)
_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join = TypeVar('_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join', bound=`namedtuple-TableJoin-table_name-column_pairs-outer_join`)

class DBService:
    __doc__: str
    db: Any
    inspector: Any
    meta: Any
    def __init__(self, db_config) -> None: ...
    def _reflect_database(self) -> None: ...
    def get_table(self, table_name) -> Dict[str, Any]: ...
    def get_tables(self) -> Dict[Any, Dict[Any, Dict[str, Any]]]: ...
    def query_table(self, table_name: str, quargs: `namedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`) -> Tuple[Any, list]: ...

class `namedtuple-ColumnPair-from_column-to_column`(tuple):
    __slots__ = ["from_column", "to_column"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    from_column: Any
    to_column: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ColumnPair-from_column-to_column`], from_column, to_column) -> `_Tnamedtuple-ColumnPair-from_column-to_column`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ColumnPair-from_column-to_column`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ColumnPair-from_column-to_column`: ...
    def _replace(self: `_Tnamedtuple-ColumnPair-from_column-to_column`, **kwds) -> `_Tnamedtuple-ColumnPair-from_column-to_column`: ...

class `namedtuple-ColumnSort-table_name-column_name-direction`(tuple):
    __slots__ = ["column_name", "direction", "table_name"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    column_name: Any
    direction: Any
    table_name: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ColumnSort-table_name-column_name-direction`], table_name, column_name, direction) -> `_Tnamedtuple-ColumnSort-table_name-column_name-direction`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ColumnSort-table_name-column_name-direction`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ColumnSort-table_name-column_name-direction`: ...
    def _replace(self: `_Tnamedtuple-ColumnSort-table_name-column_name-direction`, **kwds) -> `_Tnamedtuple-ColumnSort-table_name-column_name-direction`: ...

class `namedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`(tuple):
    __slots__ = ["column_names", "filters", "format_as_list", "group_by", "join", "page", "per_page", "sorts"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str, str, str]
    column_names: Any
    filters: Any
    format_as_list: Any
    group_by: Any
    join: Any
    page: Any
    per_page: Any
    sorts: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`], column_names, page, per_page, filters, sorts, join, group_by, format_as_list) -> `_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`: ...
    def _replace(self: `_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`, **kwds) -> `_Tnamedtuple-QueryArguments-column_names-page-per_page-filters-sorts-join-group_by-format_as_list`: ...

class `namedtuple-TableJoin-table_name-column_pairs-outer_join`(tuple):
    __slots__ = ["column_pairs", "outer_join", "table_name"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    column_pairs: Any
    outer_join: Any
    table_name: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`], table_name, column_pairs, outer_join) -> `_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`: ...
    def _replace(self: `_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`, **kwds) -> `_Tnamedtuple-TableJoin-table_name-column_pairs-outer_join`: ...

def _column_to_dict(column) -> Dict[str, Any]: ...
def apply_column_filters(query, table, join_table, filters) -> Any: ...
def apply_column_sorts(query, table, join_table, sorts: dict) -> Any: ...
def apply_group_by(query, table, join_table, group_by: list) -> Any: ...
def apply_join(query, table, join_table, join: `namedtuple-TableJoin-table_name-column_pairs-outer_join`) -> Any: ...
def column_to_dict(column) -> Dict[str, Any]: ...
def computed_column_to_dict(column) -> Dict[str, Any]: ...
def init_database(db_config) -> Any: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def names_to_columns(column_names, table, join_table) -> Any: ...
def table_to_dict(table) -> Dict[str, Any]: ...
