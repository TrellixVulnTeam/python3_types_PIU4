from typing import Any

class DebugHlsPlatform:
    OP_LATENCIES: Any = ...
    allocator: Any = ...
    scheduler: Any = ...
    def __init__(self) -> None: ...
    def onHlsInit(self, hls: Any) -> None: ...
