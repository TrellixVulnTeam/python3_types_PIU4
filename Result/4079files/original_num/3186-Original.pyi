# (generated with --quick)

from typing import Any

io: module
os: module
sys: module
yaml: module

class SettingsParser(object):
    __doc__: str
    settings: Any
    def __init__(self, path: str) -> None: ...
    def get_data_path(self) -> str: ...
    def get_ip(self) -> str: ...
    def get_meta_store_engine(self) -> str: ...
    def get_meta_store_name(self) -> str: ...
    def get_port(self) -> int: ...