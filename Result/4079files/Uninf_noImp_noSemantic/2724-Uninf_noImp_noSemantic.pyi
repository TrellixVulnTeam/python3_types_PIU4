from typing import Any

class CollectUpdateBookmarks:
    dbi: Any = ...
    def __init__(self) -> None: ...
    def original_count(self): ...
    @staticmethod
    def get_bookmarks() -> Tuple[bool, dict]: ...
    def searcher(self, dict_: Any, folder_name: Any=..., counter: Any=..., parent_folder_name: Any=..., skip: Any=...) -> list: ...
    @staticmethod
    def get_file_time(dtms: Any): ...
    def transform_json_to_df(self, json_data: Any): ...
    def main(self): ...
