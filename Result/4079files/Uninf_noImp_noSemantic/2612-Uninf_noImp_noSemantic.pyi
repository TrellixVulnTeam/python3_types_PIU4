from libbase import *
from typing import Any

__version__: str
INDEX_DB: str
STOCK_DATA_DB: str

def stocklist(flag: str = ...): ...
def querylist(db: Any, tab: Any): ...

queryindex: Any

def stockinfo(code: Any, tab: Any, db_index: Any, db_rec: Any, today: Any): ...
def updatedata() -> None: ...
def createstock(stock_list: Any) -> None: ...
def nonlisted(gen_list: Any): ...
def fetch_stock(db_index: Any, db_rec: Any, tab: Any, code: Any, today: Any) -> None: ...
def query_stock_list(): ...
