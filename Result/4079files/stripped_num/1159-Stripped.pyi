# (generated with --quick)

from typing import Any, List, TypeVar

core: Any
subprocess: module
typing: module

_TCMake = TypeVar('_TCMake', bound=CMake)

class Argument:
    name: Any
    type: Any
    value: Any
    def __init__(self, name, value, type) -> None: ...

class CMake:
    arguments: List[Argument]
    build_folder: Any
    generator: Any
    source_folder: Any
    def __init__(self, build_folder, source_folder, generator) -> None: ...
    def add_argument(self: _TCMake, name, value) -> _TCMake: ...
    def add_argument_with_type(self: _TCMake, name, value, type) -> _TCMake: ...
    def build(self) -> None: ...
    def build_cmd(self, install) -> None: ...
    def config(self) -> None: ...
    def install(self) -> None: ...
    def make_static_library(self: _TCMake) -> _TCMake: ...
    def set_install_folder(self: _TCMake, folder) -> _TCMake: ...