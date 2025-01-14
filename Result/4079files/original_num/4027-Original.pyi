# (generated with --quick)

import __future__
from typing import Any, BinaryIO, Dict, List, Match, Optional, Pattern, Tuple, TypeVar

argparse: module
platform: module
print_function: __future__._Feature
re: module

_T0 = TypeVar('_T0')

class Lexer:
    file: BinaryIO
    line_number: int
    re_addr_offset: str
    re_comment: str
    re_io_reg: str
    regexs: Tuple[Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]], Tuple[str, Pattern[str]]]
    def __init__(self, filename) -> None: ...
    def must_match(self, kind) -> Any: ...
    def next_match(self, strictly_next = ...) -> Tuple[Any, Optional[Match]]: ...

class LexerError(Exception):
    line: Any
    def __init__(self, line) -> None: ...

def convert_bytes_to_str(b: _T0) -> _T0: ...
def main() -> None: ...
def parse_file(filename) -> Tuple[List[Tuple[Any, int]], Dict[Any, List[Tuple[Any, int, int, Any]]]]: ...
def print_int_obj(val, needed_mpzs) -> None: ...
def print_periph(periph_name, periph_val, needed_qstrs, needed_mpzs) -> None: ...
def print_regs(reg_name, reg_defs, needed_qstrs, needed_mpzs) -> None: ...
def print_regs_as_submodules(reg_name, reg_defs, modules, needed_qstrs) -> None: ...
def re_match_first(regexs, line) -> Tuple[Any, Optional[Match]]: ...
