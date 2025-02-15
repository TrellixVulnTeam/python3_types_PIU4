from enum import Enum

class SyscallStatus(Enum):
    SUPPORTED: str = ...
    MISSING: str = ...
    BLOCKED: str = ...

def evaluate_statx_support() -> SyscallStatus: ...
