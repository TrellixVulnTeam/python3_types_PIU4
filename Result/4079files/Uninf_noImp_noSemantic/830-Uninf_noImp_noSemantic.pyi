from .info import ModeValue as ModeValue, Operation, WifiMode
from collections import namedtuple
from typing import Any

logger: Any

def map_files(*filters: Any, remote_dir: Any = ..., url: Any = ...): ...
def list_files(*filters: Any, remote_dir: Any = ..., url: Any = ...): ...
def map_files_raw(*filters: Any, remote_dir: Any = ..., url: Any = ...): ...
def list_files_raw(*filters: Any, remote_dir: Any = ..., url: Any = ...): ...
def count_files(remote_dir: Any = ..., url: Any = ...): ...
def memory_changed(url: Any = ...): ...
def get_ssid(url: Any = ...): ...
def get_password(url: Any = ...): ...
def get_mac(url: Any = ...): ...
def get_browser_lang(url: Any = ...): ...
def get_fw_version(url: Any = ...): ...
def get_ctrl_image(url: Any = ...): ...
def get_wifi_mode(url: Any=...) -> WifiMode: ...
def _split_file_list(text: Any) -> None: ...
def _split_file_list_raw(text: Any) -> None: ...
def _decode_time(date_val: int, time_val: int) -> Any: ...

AttrInfo = namedtuple('AttrInfo', 'archive directly volume system_file hidden_file read_only')

def _decode_attribute(attr_val: int) -> Any: ...
def _get(operation: Operation, url: Any=..., **params: Any) -> Any: ...
def _prep_get(operation: Operation, url: Any=..., **params: Any) -> Any: ...
