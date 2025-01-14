from distutils.command.build_ext import build_ext
from typing import Any

def is_new_osx(): ...

PACKAGE_DATA: Any
PACKAGES: Any
MOD_NAMES: Any
COMPILE_OPTIONS: Any
LINK_OPTIONS: Any
USE_OPENMP_DEFAULT: Any

class build_ext_options:
    def build_options(self) -> None: ...

class build_ext_subclass(build_ext, build_ext_options):
    def build_extensions(self) -> None: ...

def generate_cython(root: Any, source: Any) -> None: ...
def is_source_release(path: Any): ...
def clean(path: Any) -> None: ...
def chdir(new_dir: Any) -> None: ...
def setup_package(): ...
