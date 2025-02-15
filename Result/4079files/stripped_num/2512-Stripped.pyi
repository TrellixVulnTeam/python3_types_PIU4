# (generated with --quick)

from typing import Any, Callable, Generator

ApiCall: Any
ApiCallParams: Any
Audio: Any
Contact: Any
Document: Any
Location: Any
Message: Any
Photo: Any
State: Any
Sticker: Any
TelegramBotApi: Any
Update: Any
Video: Any
VideoNote: Any
Voice: Any

class Api:
    `async`: Any
    no_async: Api
    state: Any
    telegram_api: Any
    @staticmethod
    def _Api__api_call_hook(call, params) -> Any: ...
    def _Api__get_api_call_hook_for(self, api_call) -> Callable: ...
    def _Api__get_send_func(self, message_type) -> Any: ...
    def _Api__get_updates_offset(self) -> Any: ...
    def _Api__set_updates_offset(self, last_update_id) -> None: ...
    def _Api__should_send_message(self, message_params) -> bool: ...
    def __getattr__(self, item) -> Callable: ...
    def __init__(self, telegram_api, state) -> None: ...
    def enable_async(self, async_api) -> None: ...
    def get_pending_updates(self) -> generator: ...
    def get_updates(self, timeout = ...) -> Generator[Any, Any, None]: ...
    def send_message(self, message, **params) -> Any: ...
