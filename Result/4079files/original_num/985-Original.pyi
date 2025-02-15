# (generated with --quick)

from typing import Any, TypeVar, Union

base_path: Any
buildreq: Any
config: Any
download_path: Any
must_restart: Any
os: module
re: module
round: int
shutil: module
subprocess: module
success: int
tarball: Any
uniqueext: Any
util: module
warned_about: set

_T2 = TypeVar('_T2')

def check_for_warning_pattern(line) -> None: ...
def cleanup_req(s: str) -> str: ...
def failed_pattern(line, pattern, verbose, buildtool = ...) -> None: ...
def get_mock_cmd() -> str: ...
def get_uniqueext(dirn, dist, name: _T2) -> Union[str, _T2]: ...
def package(filemanager, mockconfig, mockopts, cleanup = ...) -> None: ...
def parse_build_results(filename, returncode, filemanager) -> None: ...
def parse_buildroot_log(filename, returncode) -> bool: ...
def reserve_path(path) -> bool: ...
def setup_workingdir(workingdir) -> None: ...
def simple_pattern(line, pattern, req) -> None: ...
def simple_pattern_pkgconfig(line, pattern, pkgconfig) -> None: ...
