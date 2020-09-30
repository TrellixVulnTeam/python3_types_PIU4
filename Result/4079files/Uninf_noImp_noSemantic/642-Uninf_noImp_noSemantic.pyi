from typing import Any, Optional

class PIP:
    @classmethod
    def run(cls, command: Any, check_output: bool = ...): ...
    @classmethod
    def run_python_m(cls, *args: Any, **kwargs: Any): ...
    @classmethod
    def run_pip_main(cls, *args: Any, **kwargs: Any): ...
    @classmethod
    def run_install(cls, cmd: Any, quiet: bool = ..., check_output: bool = ...): ...
    @classmethod
    def run_show(cls, cmd: Any, check_output: bool = ...): ...
    @classmethod
    def works(cls): ...
    @classmethod
    def get_module_version(cls, mod: Any): ...
    @classmethod
    def get_requirements(cls, file: str = ...): ...

TMPFILE: Any
LOG: Any
sh: Any
tfh: Any

def finalize_logging() -> None: ...
def bugger_off(msg: str = ..., code: int = ...) -> None: ...
def sanity_checks(optional: bool = ...) -> None: ...
def req_ensure_py3() -> None: ...
def req_ensure_encoding(): ...
def req_ensure_env() -> None: ...
def req_ensure_folders() -> None: ...
def opt_check_disk_space(warnlimit_mb: int = ...) -> None: ...
def ensure_files(): ...
def pyexec(pycom: Any, *args: Any, pycom2: Optional[Any] = ...) -> None: ...
def restart(*args: Any) -> None: ...
def main() -> None: ...