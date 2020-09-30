from typing import Any, Optional

log: Any

class Core:
    config: Any = ...
    session: Any = ...
    hooks: Any = ...
    state_dir: Any = ...
    session_stats_future: Any = ...
    torrent_data: Any = ...
    alert: Any = ...
    resume_data: Any = ...
    torrent: Any = ...
    def __init__(self, config: Any, state_dir: Optional[Any] = ...) -> None: ...
    async def start(self, settings: Optional[Any] = ...) -> None: ...
    async def stop(self) -> None: ...
    async def save_session_state(self) -> None: ...
    async def load_session_state(self) -> None: ...
    async def on_session_stats_alert(self, alert: Any) -> None: ...
    async def get_session_stats(self): ...
    def get_torrent_tags(self, info_hash: Any): ...
    async def on_status_notification_alert(self, alert: Any) -> None: ...
    async def on_state_changed_alert(self, alert: Any) -> None: ...