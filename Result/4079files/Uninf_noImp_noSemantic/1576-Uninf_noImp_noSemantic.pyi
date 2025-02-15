import analytics
from collections import namedtuple
from typing import Any

JSONDecodeError = ValueError
TWSE_BASE_URL: str
TPEX_BASE_URL: str

DATATUPLE = namedtuple('Data', ['date', 'capacity', 'turnover', 'open', 'high', 'low', 'close', 'change', 'transaction'])

class BaseFetcher:
    def fetch(self, year: Any, month: Any, sid: Any, retry: Any) -> None: ...
    def _convert_date(self, date: Any): ...
    def _make_datatuple(self, data: Any) -> None: ...
    def purify(self, original_data: Any) -> None: ...

class TWSEFetcher(BaseFetcher):
    REPORT_URL: Any = ...
    def __init__(self) -> None: ...
    def fetch(self, year: int, month: int, sid: str, retry: int=...) -> Any: ...
    def _make_datatuple(self, data: Any): ...
    def purify(self, original_data: Any): ...

class TPEXFetcher(BaseFetcher):
    REPORT_URL: Any = ...
    def __init__(self) -> None: ...
    def fetch(self, year: int, month: int, sid: str, retry: int=...) -> Any: ...
    def _convert_date(self, date: Any): ...
    def _make_datatuple(self, data: Any): ...
    def purify(self, original_data: Any): ...

class Stock(analytics.Analytics):
    sid: Any = ...
    fetcher: Any = ...
    raw_data: Any = ...
    data: Any = ...
    def __init__(self, sid: str, initial_fetch: bool=...) -> None: ...
    def _month_year_iter(self, start_month: Any, start_year: Any, end_month: Any, end_year: Any) -> None: ...
    def fetch(self, year: int, month: int) -> Any: ...
    def fetch_from(self, year: int, month: int) -> Any: ...
    def fetch_31(self): ...
    @property
    def date(self): ...
    @property
    def capacity(self): ...
    @property
    def turnover(self): ...
    @property
    def price(self): ...
    @property
    def high(self): ...
    @property
    def low(self): ...
    @property
    def open(self): ...
    @property
    def close(self): ...
    @property
    def change(self): ...
    @property
    def transaction(self): ...
