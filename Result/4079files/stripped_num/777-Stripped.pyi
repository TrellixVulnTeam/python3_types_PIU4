# (generated with --quick)

import __future__
from typing import Any, List, TypeVar

BOOTSTRAPPER: Any
BUCKFILESYSTEM: Any
BUCK_BINARY_HASH: Any
BuckTool: Any
MODULES_DIR: str
MODULES_RESOURCES_DIR: str
MovableTemporaryFile: Any
PEX_ONLY_EXPORTED_RESOURCES: list
Resource: Any
SERVER: Any
errno: module
file_locks: module
json: module
os: module
pkg_resources: module
print_function: __future__._Feature
shutil: module
stat: module
tempfile: module

_TBuckPackage = TypeVar('_TBuckPackage', bound=BuckPackage)

class BuckPackage(Any):
    _lock_file: Any
    _resource_subdir: Any
    def _BuckPackage__create_dir(self, dir) -> None: ...
    def __enter__(self: _TBuckPackage) -> _TBuckPackage: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, buck_project, buck_reporter) -> None: ...
    def _get_bootstrap_classpath(self) -> Any: ...
    def _get_buck_binary_hash(self) -> str: ...
    def _get_buck_git_commit(self) -> Any: ...
    def _get_buckfilesystem_classpath(self) -> Any: ...
    def _get_exported_resources(self) -> Any: ...
    def _get_extra_java_args(self) -> List[str]: ...
    def _get_java_classpath(self) -> Any: ...
    def _get_package_info(self) -> Any: ...
    def _get_resource(self, resource) -> Any: ...
    def _get_resource_dir(self) -> str: ...
    def _get_resource_lock_path(self) -> str: ...
    def _get_resource_subdir(self) -> Any: ...
    def _has_resource(self, resource) -> bool: ...
    def _unpack_dir(self, resource_dir, dst_dir) -> None: ...
    def _unpack_modules(self) -> None: ...
    def _unpack_resource(self, resource_path, resource_name, resource_executable) -> None: ...
