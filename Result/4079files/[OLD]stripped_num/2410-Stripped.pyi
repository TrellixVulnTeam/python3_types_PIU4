# (generated with --quick)

import csv
from typing import Any, Callable, Iterable, Type, TypeVar

DictReader: Type[csv.DictReader]
EmailHunterClient: Any
THROTTLE: float
argparse: module
json: module
time: module

_S = TypeVar('_S')
_T = TypeVar('_T')

def exist(client, email, print_header = ..., is_file_output = ...) -> None: ...
def generate(client, domain, first_name, last_name, print_header = ..., is_file_output = ...) -> None: ...
def handle_cli(command, api_key, domain = ..., offset = ..., type = ..., first_name = ..., last_name = ..., email = ..., file = ...) -> None: ...
def handle_exist_file(client, reader) -> None: ...
def handle_generate_file(client, reader) -> None: ...
def handle_search_file(client, reader) -> None: ...
def main() -> None: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
def reduce_sources(sources) -> str: ...
def search(client, domain, offset, type_, print_header = ..., is_file_output = ...) -> None: ...
def validate_exist_file(reader) -> bool: ...
def validate_generate_file(reader) -> bool: ...
def validate_search_file(reader) -> bool: ...
