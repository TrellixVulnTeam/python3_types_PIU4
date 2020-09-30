# (generated with --quick)

from typing import Callable, Iterable, List, Optional, Sequence, TypeVar, Union

BLUE: str
CLEAR: str
CYAN: str
GREEN: str
RED: str
WHITE: str
YELLOW: str
hashlib: module
operator: module
os: module
sys: module

_S = TypeVar('_S')
_T = TypeVar('_T')
_T0 = TypeVar('_T0')

def add_keys(data_dict, key, value = ...) -> None: ...
def check_string_in_file(file_name, searched_string) -> bool: ...
def diff_files(file1, file2) -> List[str]: ...
def format_string_argument(argument: _T0) -> Optional[Union[str, _T0]]: ...
def get_appflow_folder() -> str: ...
def get_env_color_string(env) -> str: ...
def get_file_list(_dir) -> list: ...
def get_from_dict(data_dict: _T0, key) -> Union[Sequence, _T0]: ...
def get_md5_folder(tenant) -> str: ...
def get_md5_sum(file_name) -> str: ...
def get_provision_color_string(command, tenant, env) -> str: ...
def get_tenant_dir(tenant) -> str: ...
def get_tenant_env_dir(tenant, env) -> str: ...
def get_vault_file(tenant, env) -> str: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
def rm_in_dict(data_dict, key) -> bool: ...
def safe_remove(file_name) -> None: ...
def set_in_dict(data_dict, key, value) -> None: ...
def write_md5_sum(file_name, md5_store_file) -> None: ...
def yes_no(question, default = ...) -> bool: ...