from typing import Any

def fix_name(name: str) -> str: ...
def remove_double_underscore(text: str) -> str: ...
def replace_double_greater(template_name: Any): ...
def get_c_name(name: str) -> str: ...
def pascal_to_stl(pascal_name: str) -> str: ...
def format_type(type_name: Any): ...
def bool_to_str(value: bool) -> str: ...
def replace_template_to_filename(template_name: Any): ...
def get_template_name(type_name: Any): ...
def get_template_tail(type_name: Any): ...
def get_template_arguments_count(type_name: Any): ...
def get_template_argument(type_name: Any, argument_index: Any): ...
def replace_template_argument(type_name: Any, argument_index: Any, new_value: Any): ...
def if_required_then_add_empty_line(first_flag: bool, out: Any) -> bool: ...
def include_headers(out: Any, headers: Any) -> None: ...
def get_full_method_name(method: Any) -> [str]: ...

class BeautifulCapiException(Exception):
    message: Any = ...
    def __init__(self, message: Any) -> None: ...
