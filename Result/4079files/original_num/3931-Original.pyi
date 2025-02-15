# (generated with --quick)

from typing import Any, Dict, List, Optional, Pattern, Tuple, Type, TypeVar

datetime: module
json: module
owncloud: Any
re: module
timedelta: Type[datetime.timedelta]

_TWeeelabLogs = TypeVar('_TWeeelabLogs', bound=WeeelabLogs)

class WeeelabLine:
    duration: str
    inlab: bool
    regex: Pattern[str]
    text: str
    time_in: str
    time_out: Optional[str]
    username: str
    def __init__(self, line: str) -> None: ...
    def day(self) -> str: ...
    def duration_minutes(self) -> int: ...

class WeeelabLogs:
    error: Optional[str]
    log: List[WeeelabLine]
    log_base: str
    log_last_update: Any
    log_path: str
    oc: Any
    old_log: List[WeeelabLine]
    old_logs_month: int
    old_logs_year: int
    user_bot_path: str
    user_path: str
    users: Any
    def __init__(self, oc, log_path: str, log_base: str, user_path: str, user_bot_path: str) -> None: ...
    def count_time_all(self) -> Dict[nothing, Any]: ...
    def count_time_month(self) -> Dict[nothing, Any]: ...
    def count_time_user(self, username) -> Tuple[Any, Any]: ...
    def get_entries_inlab(self) -> List[nothing]: ...
    def get_entry_from_tid(self, user_id: str) -> Any: ...
    def get_entry_from_username(self, username: str) -> Any: ...
    def get_log(self: _TWeeelabLogs) -> _TWeeelabLogs: ...
    @staticmethod
    def get_name_and_surname(user_entry: dict) -> Any: ...
    def get_old_logs(self) -> None: ...
    def get_users(self: _TWeeelabLogs) -> _TWeeelabLogs: ...
    @staticmethod
    def mm_to_hh_mm(minutes) -> Tuple[str, str]: ...
    def store_new_user(self, tid, name: str, surname: str, username: str) -> None: ...
    def try_get_id(self, username: str) -> Any: ...
    def try_get_name_and_surname(self, username: str) -> Any: ...
    def update_old_logs(self, max_month, max_year) -> None: ...
