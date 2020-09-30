from typing import Any, Callable, Dict, List, TypeVar

PandasDataFrame = TypeVar('DataFrame')
CollectionsOrderedDict = TypeVar('OrderedDict')
__author__: str
__copyright__: str
__credits__: Any
__license__: str
__version__: str
__maintainer__: str
__email__: str
__status__: str

class TextFile:
    __logger: Any = ...
    __path: Any = ...
    __max_width: Any = ...
    def __init__(self, max_width: int=...) -> None: ...
    def set(self, path: str, title: str, ext: str) -> Any: ...
    def reset(self) -> None: ...
    def exists(self) -> bool: ...
    def read(self, skip: int) -> List: ...
    def __read_array(self, skip: int) -> List: ...
    def append(self, data: Callable[[List, Dict, PandasDataFrame], None]) -> Any: ...
    def __append_dataframe(self, data: PandasDataFrame, label: str=...) -> Any: ...
    def __append_pretty(self, data: Callable[[List, str], None]) -> Any: ...
    def __append_pretty_dict(self, data: Callable[[Dict, CollectionsOrderedDict], None], label: str=...) -> Any: ...
    def size(self) -> int: ...