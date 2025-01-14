# (generated with --quick)

import __future__
from typing import Any, Coroutine, List

EVENT_HOMEASSISTANT_START: Any
REQUIRED_PYTHON_VER: Any
RESTART_EXIT_CODE: Any
__version__: Any
argparse: module
monkey_patch: Any
os: module
platform: module
print_function: __future__._Feature
subprocess: module
sys: module
threading: module

def check_pid(pid_file: str) -> None: ...
def closefds_osx(min_fd: int, max_fd: int) -> None: ...
def cmdline() -> List[str]: ...
def daemonize() -> None: ...
def ensure_config_file(config_dir: str) -> str: ...
def ensure_config_path(config_dir: str) -> None: ...
def get_arguments() -> argparse.Namespace: ...
def main() -> int: ...
def set_loop() -> None: ...
def setup_and_run_hass(config_dir: str, args: argparse.Namespace) -> Coroutine[Any, Any, int]: ...
def try_to_restart() -> None: ...
def validate_python() -> None: ...
def write_pid(pid_file: str) -> None: ...
