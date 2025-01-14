import subprocess
from typing import Any

class LeosacRunner(subprocess.Popen):
    out: str = ...
    err: str = ...
    def __init__(self, config_file_path: Any, valgrind: bool = ...) -> None: ...
    def run_at_most(self, timer: Any) -> bool: ...
    def run_for(self, timer: Any) -> bool: ...
    def interrupt(self) -> None: ...
    def wait_abort(self, timeout: Any) -> bool: ...
    def append_output(self, out: Any, err: Any) -> None: ...
