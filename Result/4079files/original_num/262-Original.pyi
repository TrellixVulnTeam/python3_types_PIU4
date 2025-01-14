# (generated with --quick)

from typing import Tuple, Union

argparse: module
json: module
requests: module
time: module

class RancherUpgradeException(Exception): ...

class RancherUpgradeFailException(Exception): ...

class RancherUpgradeOptions:
    rancher_access_key: str
    rancher_secret_key: str
    rancher_url: str
    retries: int
    service_name: str
    sleep_time: int
    stack_name: str
    def __init__(self, stack_name: str, service_name: str, rancher_url: str, rancher_access_key: str, rancher_secret_key: str, *, retries: int = ..., sleep_time: int = ...) -> None: ...

def check_upgrading_status(config: RancherUpgradeOptions, service_id: str) -> Union[RancherUpgradeFailException, str]: ...
def do_finish_request_upgrade(config: RancherUpgradeOptions, service_id: str) -> None: ...
def do_request_upgrade(config: RancherUpgradeOptions, service_id: str, payload: dict) -> None: ...
def do_rollback(config: RancherUpgradeOptions, service_id: str) -> None: ...
def do_tasks(config: RancherUpgradeOptions) -> None: ...
def get_service_info(config: RancherUpgradeOptions, stack_id: str) -> Union[RancherUpgradeException, Tuple[str, dict]]: ...
def get_stack_id(config: RancherUpgradeOptions) -> Union[RancherUpgradeException, str]: ...
def main() -> None: ...
def make_upgrade(config: RancherUpgradeOptions, service_id: str, payload: dict) -> None: ...
