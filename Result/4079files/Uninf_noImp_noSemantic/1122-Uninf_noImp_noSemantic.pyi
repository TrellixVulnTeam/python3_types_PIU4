from typing import Any

def set_size(fd: Any, row: Any, col: Any, xpix: int = ..., ypix: int = ...) -> None: ...
def get_size(fd: Any): ...

STDIN: int
CLONE_NEWNS: int
CLONE_NEWUTS: int
CLONE_NEWIPC: int
CLONE_NEWUSER: int
CLONE_NEWPID: int
CLONE_NEWNET: int
CLONE_NEWCGROUP: int
MS_RDONLY: int
MS_NOSUID: int
MS_NODEV: int
MS_NOEXEC: int
MS_BIND: int
MS_REC: int
MS_PRIVATE: int
MS_STRICTATIME: int
MNT_FORCE: int
MNT_DETACH: int
MNT_EXPIRE: int
UMOUNT_NOFOLLOW: int
_libc: Any

def require_root(fn: Any): ...
def sys_unshare(flags: Any) -> None: ...
def sys_mount(*kargs: Any) -> None: ...
def sys_umount(target: Any, flags: int = ...) -> None: ...
def sethostname(hostname: str) -> Any: ...

class Pipe:
    def __init__(self) -> None: ...
    def close_read(self) -> None: ...
    def close_write(self) -> None: ...
    def read(self, n: Any): ...
    def write(self, bs: Any) -> None: ...