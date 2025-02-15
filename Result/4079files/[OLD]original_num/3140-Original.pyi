# (generated with --quick)

from typing import Any, Dict, Tuple, Union

datetime: Any
json: module
pytz: module
timedelta: Any

class ToLab:
    local_tz: Union[pytz._DstTzInfo, pytz._StaticTzInfo, pytz._UTCclass]
    oc: Any
    tolab_file: Any
    tolab_path: str
    def __init__(self, oc, tolab_path: str) -> None: ...
    def _create_entry(self, username: str, telegram_id: int, time: str, day: int) -> Tuple[Dict[str, Any], Any]: ...
    def _delete_user(self, telegram_id) -> None: ...
    def check_tolab(self, people_inlab: set) -> int: ...
    def delete_entry(self, telegram_id: int) -> None: ...
    def save(self, entries: list) -> None: ...
    def set_entry(self, username: str, telegram_id: int, time: str, day: int) -> int: ...
