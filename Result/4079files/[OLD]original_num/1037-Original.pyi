# (generated with --quick)

import proxy.remote
import subprocess
from typing import Any, Callable, Optional, Tuple, Type

CalledProcessError: Type[subprocess.CalledProcessError]
RemoteInfo: Type[proxy.remote.RemoteInfo]
Runner: Any

def create_new_deployment(runner, deployment_arg: str, expose, add_custom_nameserver: bool) -> Tuple[str, str]: ...
def existing_deployment(runner, deployment_arg: str, expose, add_custom_nameserver: bool) -> Tuple[str, Optional[str]]: ...
def get_remote_info(runner, deployment_name: str, deployment_type: str, run_id: Optional[str] = ...) -> proxy.remote.RemoteInfo: ...
def setup(runner, args) -> Callable[[Any], proxy.remote.RemoteInfo]: ...
def supplant_deployment(runner, deployment_arg: str, expose, add_custom_nameserver: bool) -> Tuple[str, str]: ...
def swap_deployment_openshift(runner, deployment_arg: str, expose, add_custom_nameserver: bool) -> Tuple[str, str]: ...