from typing import Any, Optional

REQUESTS_TIMEOUT: int

class Site:
    url_host: str = ...
    db_column: str = ...
    encode: str = ...
    suspended: int = ...
    name: Any = ...
    status: Any = ...
    cookies: Any = ...
    _EXTEND_DESCR_BEFORE: Any = ...
    _EXTEND_DESCR_THUMBNAILS: Any = ...
    _EXTEND_DESCR_MEDIAINFO: Any = ...
    _EXTEND_DESCR_CLONEINFO: Any = ...
    _ASSIST_ONLY: Any = ...
    _ASSIST_DELAY_TIME: Any = ...
    def __init__(self, status: bool, cookies: None, **kwargs: Any) -> None: ...
    def online_check(self) -> bool: ...
    @staticmethod
    def _post_torrent_file_tuple(torrent: Any): ...
    @staticmethod
    def _get_torrent(torrent: Any): ...
    def _assist_delay(self) -> None: ...
    def _get_torrent_ptn(self, torrent: Any): ...
    def get_data(self, url: Any, params: Optional[Any] = ..., bs: bool = ..., json: bool = ..., **kwargs: Any): ...
    def post_data(self, url: Any, params: Optional[Any] = ..., **kwargs: Any): ...
    def enhance_descr(self, torrent: Any, descr_text: Any, clone_id: Any): ...
    def torrent_feed(self, torrent: Any) -> None: ...
    def session_check(self) -> None: ...
    def torrent_reseed(self, torrent: Any) -> None: ...
