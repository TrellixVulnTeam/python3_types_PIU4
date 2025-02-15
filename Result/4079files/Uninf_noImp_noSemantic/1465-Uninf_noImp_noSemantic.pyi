from datetime import datetime
from gphotos.GooglePhotosMedia import GooglePhotosMedia
from gphotos.LocalData import LocalData
from gphotos.restclient import RestClient
from pathlib import Path
from typing import Any

log: Any

class GooglePhotosIndex:
    PAGE_SIZE: int = ...
    _api: Any = ...
    _root_folder: Any = ...
    _db: Any = ...
    _media_folder: Any = ...
    _use_flat_path: Any = ...
    files_indexed: int = ...
    files_index_skipped: int = ...
    latest_download: Any = ...
    start_date: Any = ...
    end_date: Any = ...
    include_video: bool = ...
    rescan: bool = ...
    favourites: bool = ...
    def __init__(self, api: RestClient, root_folder: Path, db: LocalData, photos_path: Path, use_flat_path: bool=...) -> None: ...
    def check_for_removed_in_folder(self, folder: Path) -> Any: ...
    def check_for_removed(self) -> None: ...
    def write_media_index(self, media: GooglePhotosMedia, update: bool=...) -> Any: ...
    year: Any = ...
    month: Any = ...
    day: Any = ...
    def search_media(self, page_token: int=..., start_date: datetime=..., end_date: datetime=..., do_video: bool=..., favourites: bool=...) -> dict: ...
    def index_photos_media(self) -> bool: ...
    def get_extra_meta(self) -> None: ...
