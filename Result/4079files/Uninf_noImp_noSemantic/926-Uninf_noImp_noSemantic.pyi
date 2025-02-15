from typing import Any

class Callback:
    update: Any = ...
    id: Any = ...
    query: Any = ...
    sender: Any = ...
    message: Any = ...
    _api: Any = ...
    isInline: Any = ...
    inline_message_id: Any = ...
    chat: Any = ...
    def __init__(self, update: Any) -> None: ...
    def notify(self, text: Any, alert: bool = ..., cache_time: int = ...) -> None: ...
