from argparse import Namespace
from pathlib import Path
from typing import Any

__version__: Any
APP_NAME: str
log: Any

class GooglePhotosSyncMain:
    data_store: Any = ...
    google_photos_client: Any = ...
    google_photos_idx: Any = ...
    google_photos_down: Any = ...
    google_albums_sync: Any = ...
    local_files_scan: Any = ...
    location_update: Any = ...
    _start_date: Any = ...
    _end_date: Any = ...
    auth: Any = ...
    def __init__(self) -> None: ...
    version_string: Any = ...
    parser: Any = ...
    def setup(self, args: Namespace, db_path: Path) -> Any: ...
    @classmethod
    def logging(cls: Any, args: Namespace, folder: Path) -> Any: ...
    def do_location(self, args: Namespace) -> Any: ...
    def do_sync(self, args: Namespace) -> Any: ...
    def start(self, args: Namespace) -> Any: ...
    def main(self, test_args: dict=...) -> Any: ...

def main() -> None: ...