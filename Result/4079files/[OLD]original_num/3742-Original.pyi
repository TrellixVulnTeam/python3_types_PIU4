# (generated with --quick)

from typing import Any

SESSION_URL: str
STOCKINFO_URL: str
datetime: module
get_proxies: Any
json: module
mock: bool
requests: module
sys: module
time: module
twstock: Any

def _format_stock_info(data) -> dict: ...
def _join_stock_id(stocks) -> str: ...
def get(stocks, retry = ...) -> Any: ...
def get_raw(stocks) -> dict: ...
