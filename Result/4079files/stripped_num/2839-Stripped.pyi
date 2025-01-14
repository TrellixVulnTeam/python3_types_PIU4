# (generated with --quick)

import collections
import flask.app
import flask.wrappers
from typing import Any, Iterable, Optional, Tuple, Type, TypeVar, Union

ColumnFilter: Any
ColumnFunction: Any
ColumnPair: Any
ColumnSort: Any
ComplexFilter: Any
DBService: Any
DEFAULT_PAGE: Any
DEFAULT_PER_PAGE: Any
Flask: Type[flask.app.Flask]
JoinError: Any
NotFoundError: Any
OrderedDict: Type[collections.OrderedDict]
QueryArguments: Any
SORT_DIRECTIONS: Any
SUPPORTED_FUNCS: Any
TableJoin: Any
log: logging.Logger
logging: module
request: flask.wrappers.Request

_T0 = TypeVar('_T0')

class DBController:
    app: Any
    db_service: Any
    def __init__(self, app, db_service) -> None: ...
    def chart_page(self, name) -> Union[str, Tuple[str, int]]: ...
    def get_query_args(self) -> Any: ...
    def query_api(self, name) -> Any: ...
    def register_routes(self) -> None: ...
    def table_api(self, name) -> Any: ...
    def table_page(self, name) -> Union[str, Tuple[str, int]]: ...
    def tables_api(self) -> Any: ...
    def tables_page(self) -> str: ...

def _parse_filter_obj_dict(filters, from_url = ...) -> Any: ...
def jsonify(*args, **kwargs) -> Any: ...
def parse_col_names(column_names: _T0) -> Union[list, _T0]: ...
def parse_column_func(column_string) -> Any: ...
def parse_column_funcs(column_list) -> list: ...
def parse_filter(filter_string) -> Any: ...
def parse_filter_obj(filters, from_url = ...) -> Any: ...
def parse_filters(filter_description) -> Any: ...
def parse_join(join_str, outer_join) -> Any: ...
def parse_pagination(page, per_page) -> Tuple[Any, Any]: ...
def parse_query_args(query_args) -> Tuple[list, Any, Any, Any, Any, Any, list]: ...
def parse_sort(sort_string) -> Any: ...
def parse_sorts(sort_list) -> Optional[list]: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def table_not_found(name) -> Tuple[str, int]: ...
