# (generated with --quick)

import node.create_list
import node.numeric_literal
import node.string_literal
import type.type_time
from typing import Any, Callable, Dict, NoReturn, Type, Union

List: Type[node.create_list.List]
NumericLiteral: Type[node.numeric_literal.NumericLiteral]
StringLiteral: Type[node.string_literal.StringLiteral]
TypeTime: Type[type.type_time.TypeTime]
nodes: Dict[Type[Union[float, int, list, str, tuple]], Type[Union[node.create_list.List, node.numeric_literal.NumericLiteral, node.string_literal.StringLiteral]]]
parsers: Dict[type, Callable[[Any], Any]]

def dict_literal(dic) -> NoReturn: ...
def float_literal(number) -> str: ...
def int_literal(number) -> str: ...
def list_literal(seq) -> Any: ...
def parse_item(item) -> Any: ...
def set_literal(seq) -> NoReturn: ...
def stack_literal(stack) -> Any: ...
def string_literal(string) -> str: ...
def time_literal(time) -> NoReturn: ...
def tuple_literal(seq) -> Any: ...