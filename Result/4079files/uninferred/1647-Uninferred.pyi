from typing import Any, Optional

__author__: Any
__license__: str
ARGS: Any

class TLGU:
    testing: Any = ...
    def __init__(self, testing: bool = ...) -> None: ...
    @staticmethod
    def _check_import_source() -> None: ...
    def _check_install(self) -> None: ...
    def convert(self, input_path: Optional[Any] = ..., output_path: Optional[Any] = ..., markup: Optional[Any] = ..., break_lines: bool = ..., divide_works: bool = ..., latin: bool = ..., extra_args: Optional[Any] = ...) -> None: ...
    def convert_corpus(self, corpus: Any, markup: Optional[Any] = ..., break_lines: bool = ..., divide_works: bool = ..., latin: Optional[Any] = ..., extra_args: Optional[Any] = ...) -> None: ...
    def divide_works(self, corpus: Any) -> None: ...
