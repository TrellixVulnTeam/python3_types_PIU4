# (generated with --quick)

from typing import Any, List, Match, Optional, Pattern, Sequence, Tuple

TYPESHED_HOME: str
TYPESHED_SUBDIRS: List[str]
UNSET: Any
argparse: module
itertools: module
os: module
pytype_config: module
pytype_io: module
re: module
subprocess: module
traceback: module

class PathMatcher:
    matcher: Optional[Pattern[str]]
    def __init__(self, patterns: Sequence[str]) -> None: ...
    def search(self, path: str) -> Optional[Match[str]]: ...

def _get_module_name(filename: str) -> str: ...
def _get_relative(filename: str) -> str: ...
def _is_version(path: str, version: str) -> bool: ...
def can_run(exe: str, *, args: List[str]) -> bool: ...
def check_python_exes_runnable(*, python27_exe_arg: str, python36_exe_arg: str) -> None: ...
def check_subdirs_discoverable(subdir_paths: List[str]) -> None: ...
def create_parser() -> argparse.ArgumentParser: ...
def determine_files_to_test(*, typeshed_location: str, subdir_paths: Sequence[str]) -> List[Tuple[str, int]]: ...
def load_blacklist(typeshed_location: str) -> List[str]: ...
def main() -> None: ...
def run_all_tests(*, files_to_test: Sequence[Tuple[str, int]], typeshed_location: str, python27_exe: str, python36_exe: str, print_stderr: bool, dry_run: bool) -> None: ...
def run_pytype(*, filename: str, python_version: str, python_exe: str, typeshed_location: str) -> Optional[str]: ...
