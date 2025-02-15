from typing import Any, Iterable, List, Optional, Tuple

VERSION_FILE: str
MODULE_DIR: str
LOGGER: Any

class SourceNotFoundException(Exception): ...

class SourceInfo:
    path: Any = ...
    _hash: Any = ...
    _content: Any = ...
    _requires: Any = ...
    module_name: Any = ...
    def __init__(self, path: str, module_name: str) -> None: ...
    @property
    def hash(self) -> str: ...
    @property
    def content(self) -> str: ...
    def _get_module_name(self) -> str: ...
    @property
    def requires(self) -> List[str]: ...

class CodeManager:
    __type_file: Any = ...
    __file_info: Any = ...
    def __init__(self) -> None: ...
    def register_code(self, type_name: str, instance: object) -> None: ...
    def get_object_source(self, instance: object) -> Optional[str]: ...
    def get_file_hashes(self) -> Iterable[str]: ...
    def get_file_content(self, hash: str) -> str: ...
    def get_types(self) -> Iterable[Tuple[str, List[SourceInfo]]]: ...

class CodeLoader:
    __code_dir: Any = ...
    __modules: Any = ...
    def __init__(self, code_dir: str) -> None: ...
    def load_modules(self) -> None: ...
    def __check_dir(self) -> None: ...
    def _load_module(self, mod_name: str, python_file: str, hv: str) -> None: ...
    def deploy_version(self, hash_value: str, module_name: str, module_source: str) -> None: ...
