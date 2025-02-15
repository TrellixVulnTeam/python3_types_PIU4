# (generated with --quick)

import jinja2.environment
import jinja2.loaders
from typing import Any, Callable, List, Type, TypeVar

Environment: Type[jinja2.environment.Environment]
FileSystemLoader: Type[jinja2.loaders.FileSystemLoader]
codecs: module
json: module
load_workbook: Any
os: module
string: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class ExcelConverterBase(object):
    bots: list
    data: List[nothing]
    intents: list
    namespace: Any
    outputDir: Any
    slot_types: list
    templateDir: str
    wb: Any
    worksheets: Any
    @staticmethod
    def _ExcelConverterBase__get_ascii_only_json_str(c) -> str: ...
    def __init__(self, workbook_path_name, lexjson_dir) -> None: ...
    @staticmethod
    def _get_cell_value(worksheet, address, json_encode = ...) -> str: ...
    def _get_new_line_list(self, content) -> list: ...
    def _get_newline_spilt_data(self, column, row, worksheet) -> list: ...
    def _get_single_value_cell_data(self, sheet_name, data) -> dict: ...
    def _get_variable_length_column_data(self, column, start_row, worksheet, json_encode = ...) -> List[str]: ...
    def _get_variable_length_row_data(self, column, row, worksheet, json_encode = ...) -> List[str]: ...
    def _get_worksheet(self, sheet_name) -> Any: ...
    def _render(self, filename, data, is_json) -> str: ...
    def _save_json_template(self, template_filename, save_filename, data) -> None: ...
    def _save_yaml_template(self, template_filename, save_filename, data) -> None: ...
    @abstractmethod
    def generate_json(self) -> None: ...
    def populate_simple_cell_data(self, sheet_name, data) -> dict: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
