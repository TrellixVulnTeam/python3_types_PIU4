from make_runner import MakeRunner as MakeRunner
from typing import Any

def pytest_addoption(parser: Any) -> None: ...
def gmake(tmpdir: Any): ...
def make(tmpdir: Any, request: Any): ...
