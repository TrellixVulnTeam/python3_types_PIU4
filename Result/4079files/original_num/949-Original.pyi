# (generated with --quick)

import crash.commands
from typing import Iterable, Type
import uuid

ArgumentParser: Type[crash.commands.ArgumentParser]
Command: Type[crash.commands.Command]
CommandLineError: Type[crash.commands.CommandLineError]
argparse: module

class BtrfsCommand(crash.commands.Command):
    __doc__: str
    def __init__(self, name: str) -> None: ...
    def list_btrfs(self, args: argparse.Namespace) -> None: ...

class _Parser(crash.commands.ArgumentParser): ...

def btrfs_fsid(super_block, force: bool = ...) -> uuid.UUID: ...
def btrfs_metadata_uuid(sb, force: bool = ...) -> uuid.UUID: ...
def for_each_super_block() -> Iterable: ...
def super_fstype(sb) -> str: ...