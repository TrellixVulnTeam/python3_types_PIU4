from typing import Any

class Crawler:
    mypath: Any = ...
    notExistDays: Any = ...
    headers: Any = ...
    bamboo_id: Any = ...
    bamboo_nickname: Any = ...
    first_date: Any = ...
    first_day: Any = ...
    def __init__(self, bamboo_tuple: Any, first_date: Any) -> None: ...
    def getDataWithDate(self, date: Any, page: Any): ...
    def writeContent(self, post_num: Any) -> None: ...
    def writeJSON(self, day: Any, post_num: Any): ...
