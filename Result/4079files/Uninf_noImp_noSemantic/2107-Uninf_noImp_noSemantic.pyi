from typing import Any

CURRENT_DIR: Any

class BaseManage:
    commands_package_path: Any = ...
    store_cls: Any = ...
    _modules: Any = ...
    _commands: Any = ...
    _logger: Any = ...
    def __init__(self) -> None: ...
    @property
    def commands(self): ...
    @property
    def config(self): ...
    @property
    def debug(self): ...
    def help(self) -> None: ...
    def run(self): ...
    def _run_command(self, command: Any, *args: Any) -> None: ...
    def _parse_manage_arguments(self): ...
    @property
    def logger(self): ...

def main(manager_cls: Any) -> None: ...
