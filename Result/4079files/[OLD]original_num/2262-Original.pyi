# (generated with --quick)

import asyncio.events
import collections
import types
from typing import Any, Callable, Dict, List, Optional, Tuple, Type

aiohttp: Any
async_timeout: Any
asyncio: module
custom_exceptions: Any
deque: Type[collections.deque]
json: module
ratelimit_key_queue_map: Dict[str, collections.deque[float]]
ratelimit_key_time_map: Dict[str, float]
time: module
url_parser: module

def _add_request_parameters(func) -> Callable: ...
def _get_float(data, default) -> float: ...
def _get_int(data, default) -> int: ...
def basic_request(loop: asyncio.events.AbstractEventLoop, api_key: str, timeout_seconds: float, endpoint: str, *args, method: str = ..., handle_ratelimiting: bool = ..., _cur_retry: int = ..., **kwargs) -> coroutine: ...
def exc_info() -> Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[types.TracebackType]]: ...
def format_exception(etype: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[types.TracebackType], limit: Optional[int] = ..., chain: bool = ...) -> List[str]: ...
def get_platforms(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_player(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_player_batch(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_playlists(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_ranked_leaderboard(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_seasons(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_stats_leaderboard(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def get_tiers(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
def search_players(*args, api_key: str = ..., handle_ratelimiting: bool = ..., timeout_seconds: float = ..., api_version: int = ..., loop: Optional[asyncio.events.AbstractEventLoop] = ..., **kwargs) -> coroutine: ...
