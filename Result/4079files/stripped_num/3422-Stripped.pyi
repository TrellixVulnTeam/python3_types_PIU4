# (generated with --quick)

import sqlite3.dbapi2
from typing import Any, Dict, List, Optional, Tuple, TypeVar

CommandError: Any
SessionLoadException: Any
asyncio: module
bisect: module
collections: module
copy: module
ctx: Any
flowfilter: Any
http: Any
matchall: Any
orders: List[str]
os: module
pkg_data: Any
protobuf: Any
shutil: module
sqlite3: module
tempfile: module
types: Any
typing: module

_T0 = TypeVar('_T0')

class KeyifyList(object):
    inner: Any
    key: Any
    def __getitem__(self, k) -> Any: ...
    def __init__(self, inner, key) -> None: ...
    def __len__(self) -> int: ...

class Session:
    _FP_DECREMENT: float
    _FP_DEFAULT: float
    _FP_RATE: int
    _flush_period: float
    _flush_rate: int
    _hot_store: collections.OrderedDict
    _order_store: Dict[Any, Dict[str, Any]]
    _view: Any
    db_store: Optional[SessionDB]
    filter: Any
    order: Any
    started: bool
    def __init__(self) -> None: ...
    @staticmethod
    def _generate_order(o, f) -> Any: ...
    def _refilter(self) -> None: ...
    def _store_order(self, f) -> None: ...
    def _writer(self) -> coroutine: ...
    def clear_storage(self) -> None: ...
    def configure(self, updated) -> None: ...
    def error(self, f) -> None: ...
    def intercept(self, f) -> None: ...
    def kill(self, f) -> None: ...
    def load(self, loader) -> None: ...
    def load_storage(self, ids = ...) -> Any: ...
    def load_view(self) -> list: ...
    def request(self, f) -> None: ...
    def response(self, f) -> None: ...
    def resume(self, f) -> None: ...
    def running(self) -> None: ...
    def set_filter(self, input_filter) -> None: ...
    def set_order(self, order) -> None: ...
    def store_count(self) -> int: ...
    def update(self, flows) -> None: ...
    def update_view(self, f) -> None: ...

class SessionDB:
    __doc__: str
    body_ledger: set
    con: Optional[sqlite3.dbapi2.Connection]
    content_threshold: int
    id_ledger: set
    live_components: Dict[Any, Tuple[Any, Any, Any, Any, Any, Any, Optional[Tuple[Any, Any, Any]], Any]]
    tempdir: Optional[str]
    type_mappings: Dict[str, Dict[int, str]]
    def __contains__(self, fid) -> bool: ...
    def __del__(self) -> None: ...
    def __init__(self, db_path = ...) -> None: ...
    def __len__(self) -> int: ...
    def _create_session(self) -> None: ...
    def _disassemble(self, flow) -> None: ...
    def _load_session(self, path) -> None: ...
    def _reassemble(self, flow: _T0) -> _T0: ...
    def clear(self) -> None: ...
    @staticmethod
    def is_session_db(path) -> bool: ...
    def retrieve_flows(self, ids = ...) -> list: ...
    def store_flows(self, flows) -> None: ...