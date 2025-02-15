from typing import Any, Optional

BASEDIR: Any

def get_basedir(): ...
def dir_function() -> None: ...

class TestDirectory:
    basedir: Any = ...
    name: Any = ...
    path: Any = ...
    settings: Any = ...
    def __init__(self, basedir: Any) -> None: ...
    def activate(self): ...
    def remove(self) -> None: ...

def testdir_session() -> None: ...
def testdir_class() -> None: ...
def testdir_function() -> None: ...

class Project:
    testdir_fixture: Any = ...
    testdir: Any = ...
    name: Any = ...
    path: Any = ...
    settings: Any = ...
    def __init__(self, testdir_fixture: Any) -> None: ...
    def values(self): ...
    def activate(self): ...
    def remove(self) -> None: ...

def project_session(testdir_session: Any) -> None: ...
def project_class(testdir_session: Any) -> None: ...
def project_function(testdir_session: Any) -> None: ...
def project_function_clean(testdir_function: Any) -> None: ...
def test_utils() -> None: ...

class TestUtils:
    @staticmethod
    def create_empty_file(path: Any, filename: Any) -> None: ...
    @staticmethod
    def random_string(length: Any, prefix: str = ...): ...
    @staticmethod
    def random_numeric_string(length: Any, prefix: str = ...): ...
    @staticmethod
    def run_command(cmd: Any): ...
    @staticmethod
    def set_project_setting(testdir: Any, setting: Any, setting_value: Any) -> None: ...
    @staticmethod
    def create_test(testdir: Any, project: Any, parents: Any, name: Any, content: Optional[Any] = ...): ...
    @staticmethod
    def create_suite(testdir: Any, project: Any, name: Any, content: Optional[Any] = ..., tests: Optional[Any] = ..., processes: int = ..., browsers: Optional[Any] = ..., environments: Optional[Any] = ..., tags: Optional[Any] = ...) -> None: ...

def pytest_addoption(parser: Any) -> None: ...
def pytest_runtest_setup(item: Any) -> None: ...
