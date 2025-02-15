import unittest
from distutils.tests import support
from typing import Any

class FakeCompiler:
    def library_dir_option(self, dir: Any): ...
    def runtime_library_dir_option(self, dir: Any): ...
    def find_library_file(self, dirs: Any, lib: Any, debug: int = ...): ...
    def library_option(self, lib: Any): ...

class CCompilerTestCase(support.EnvironGuard, unittest.TestCase):
    def test_gen_lib_options(self) -> None: ...
    def test_debug_print(self) -> None: ...
    exes: Any = ...
    def test_customize_compiler(self) -> None: ...

def test_suite(): ...
