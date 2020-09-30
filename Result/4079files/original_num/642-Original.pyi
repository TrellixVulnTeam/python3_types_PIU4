# (generated with --quick)

import __future__
import shutil
from typing import Any, Callable, IO, NoReturn, Optional, Union

LOG: logging.Logger
TMPFILE: IO[str]
importlib: module
logging: module
os: module
pathlib: module
print_function: __future__._Feature
sh: logging.StreamHandler
subprocess: module
sys: module
tempfile: module
tfh: nothing
time: module
traceback: module

class PIP(object):
    __doc__: str
    @classmethod
    def get_module_version(cls, mod) -> Any: ...
    @classmethod
    def get_requirements(cls, file = ...) -> list: ...
    @classmethod
    def run(cls, command, check_output = ...) -> Union[bytes, int]: ...
    @classmethod
    def run_install(cls, cmd, quiet = ..., check_output = ...) -> Any: ...
    @classmethod
    def run_pip_main(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def run_python_m(cls, *args, **kwargs) -> Union[bytes, int]: ...
    @classmethod
    def run_show(cls, cmd, check_output = ...) -> Any: ...
    @classmethod
    def works(cls) -> bool: ...

def bugger_off(msg = ..., code = ...) -> NoReturn: ...
def disk_usage(path: Union[str, _PathLike[str]]) -> shutil._ntuple_diskusage: ...
def ensure_files() -> Optional[bool]: ...
def finalize_logging() -> None: ...
def main() -> None: ...
def opt_check_disk_space(warnlimit_mb = ...) -> None: ...
def pyexec(pycom, *args, pycom2 = ...) -> NoReturn: ...
def req_ensure_encoding() -> None: ...
def req_ensure_env() -> None: ...
def req_ensure_folders() -> None: ...
def req_ensure_py3() -> None: ...
def restart(*args) -> NoReturn: ...
def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
def sanity_checks(optional = ...) -> None: ...