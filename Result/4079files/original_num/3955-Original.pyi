# (generated with --quick)

from typing import Any

datetime: module
sqlite3: module

class libJournal:
    db_location: str
    entry_number: int
    def __init__(self) -> None: ...
    @staticmethod
    def _libJournal__entries_iterate(entry_dict) -> None: ...
    @staticmethod
    def _libJournal__get_date() -> str: ...
    @staticmethod
    def _libJournal__get_time() -> str: ...
    def _libJournal__set_latest_entry_number(self) -> None: ...
    @staticmethod
    def create_db(db_name: str) -> None: ...
    def delete_by_number(self, entry_number: int) -> None: ...
    def entries_all(self) -> list: ...
    def entry_new(self, entry_title: str, entry_content: str) -> None: ...
    def most_recent_entry(self) -> Any: ...
    def read_by_date(self, entry_date: str, entry_location: int) -> Any: ...
    def read_by_number(self, entry_number: int) -> Any: ...
    def read_by_title(self, entry_name: str, entry_location: int) -> Any: ...
    def search_by_date(self, entry_date: str) -> list: ...
    def search_by_number(self, entry_number: int) -> list: ...
    def search_by_title(self, entry_title: str) -> list: ...
    def set_db_location(self, db_name: str) -> None: ...
    @staticmethod
    def setup_db(db_name: str) -> None: ...