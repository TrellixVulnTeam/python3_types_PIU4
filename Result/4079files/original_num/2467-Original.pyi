# (generated with --quick)

from typing import Any, Callable

Runner: Any
SUDO_FOR_DOCKER: Any
launch_inject: Any
launch_vpn: Any
run_docker_command: Any

def check_local_command(runner, command: str) -> None: ...
def setup(runner, args) -> Callable[[Any, Any, Any, Any, Any, Any, Any], Any]: ...
def setup_container(runner, args) -> Callable[[Any, Any, Any, Any, Any, Any, Any], Any]: ...
def setup_inject(runner, args) -> Callable[[Any, Any, Any, Any, Any, Any, Any], Any]: ...
def setup_vpn(runner, args) -> Callable[[Any, Any, Any, Any, Any, Any, Any], Any]: ...
