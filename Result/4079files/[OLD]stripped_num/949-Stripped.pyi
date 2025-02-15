# (generated with --quick)

import crash.commands
from typing import Any, Generator, Type

ArgumentParser: Type[crash.commands.ArgumentParser]
Command: Type[crash.commands.Command]
CommandLineError: Type[crash.commands.CommandLineError]
argparse: module

class BtrfsCommand(crash.commands.Command):
    __doc__: str
    def __init__(self, name) -> None: ...
    def execute(self, args) -> None: ...
    def list_btrfs(self, args) -> None: ...

class _Parser(crash.commands.ArgumentParser): ...

def btrfs_fsid(super_block, force = ...) -> Any: ...
def btrfs_metadata_uuid(sb, force = ...) -> Any: ...
def for_each_super_block() -> Generator[Any, Any, None]: ...
def super_fstype(sb) -> Any: ...
