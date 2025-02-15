# (generated with --quick)

import collections
import typing
from typing import Any, Callable, Dict, Iterable, List, Optional, Sized, Tuple, TypeVar, Union

TypeImport = `namedtuple-TypeImport-module-symbol`

Block: Any
BlockType: Any
ConfigError: Any
DatatypeError: Any
Entity: Any
Enumeration: Any
Model: Any
PYTHON_BASE_TYPES: Dict[str, str]
PYTHON_TYPE_IMPORTS: Dict[str, `namedtuple-TypeImport-module-symbol`]
Property: Any
Type: Any
Writer: Any
decamelize: Any
re: module
to_bool: Any
to_identifier: Any

_Tnamedtuple-TypeImport-module-symbol = TypeVar('_Tnamedtuple-TypeImport-module-symbol', bound=`namedtuple-TypeImport-module-symbol`)

class PythonWriter(Any):
    block_types: List[str]
    entities_module: Optional[str]
    entity_per_module: Any
    enums_module: Optional[str]
    model: Any
    def __init__(self, model, variables: Optional[Dict[str, str]] = ...) -> None: ...
    def _entity_import(self, entity) -> Optional[`namedtuple-TypeImport-module-symbol`]: ...
    def _enum_import(self, enum) -> Optional[`namedtuple-TypeImport-module-symbol`]: ...
    def comment(self, text: str) -> Any: ...
    def create_block(self, block_type: str, entities: Optional[List[str]] = ...) -> Any: ...
    def default_value(self, prop) -> str: ...
    def docstring(self, text: str) -> str: ...
    def entity_type_imports(self, entity) -> List[`namedtuple-TypeImport-module-symbol`]: ...
    def eq_method(self, entity) -> Any: ...
    def init_argument(self, prop) -> str: ...
    def init_assignment(self, prop) -> Any: ...
    def init_method(self, entity) -> Any: ...
    def literal(self, value: str, type) -> str: ...
    def type_annotation(self, type) -> str: ...
    def type_imports(self, type) -> List[`namedtuple-TypeImport-module-symbol`]: ...
    def typed_property(self, prop, wrap: Optional[str] = ...) -> str: ...
    def write_class(self, entity) -> Any: ...
    def write_class_file(self, entities: list) -> Any: ...
    def write_classes(self, entities: list) -> Any: ...
    def write_enum(self, enum) -> Any: ...
    def write_enums_file(self) -> Any: ...

class `namedtuple-TypeImport-module-symbol`(tuple):
    __slots__ = ["module", "symbol"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    module: Any
    symbol: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: typing.Type[`_Tnamedtuple-TypeImport-module-symbol`], module, symbol) -> `_Tnamedtuple-TypeImport-module-symbol`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: typing.Type[`_Tnamedtuple-TypeImport-module-symbol`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TypeImport-module-symbol`: ...
    def _replace(self: `_Tnamedtuple-TypeImport-module-symbol`, **kwds) -> `_Tnamedtuple-TypeImport-module-symbol`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def sort_by_default(props: list) -> list: ...
