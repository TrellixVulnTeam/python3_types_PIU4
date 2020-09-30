# (generated with --quick)

from typing import Any, List, Type

ES_HOSTS: Any
EXCHANGE_LIST_COL: List[str]
FOOLTRADER_STORE_PATH: Any
KAFKA_HOST: Any
KafkaProducer: Any
connections: Any
datetime: Type[datetime.datetime]
e: nothing
es_client: Any
get_event_path: Any
get_security_list: Any
kafka_producer: Any
logger: Any
os: module
pd: Any
pd_utils: module
technical: Any
to_security_item: Any

def __getattr__(name) -> Any: ...
def df_for_date_range(df, start_date = ..., end_date = ...) -> Any: ...
def ema(security_item, start_date, end_date, level = ..., fuquan = ..., source = ..., window = ..., col = ..., return_all = ..., return_col = ...) -> Any: ...
def get_event(security_item, event_type = ..., start_date = ..., end_date = ..., index = ...) -> Any: ...
def get_event_dir(item) -> str: ...
def get_exchange_cache_dir(security_type = ..., exchange = ..., the_year = ..., data_type = ...) -> str: ...
def get_exchange_dir(security_type = ..., exchange = ...) -> Any: ...
def get_finance_dir(item) -> str: ...
def get_finance_forecast_event(security_item, start_date = ..., end_date = ...) -> Any: ...
def get_finance_report_event(security_item, index = ..., start_date = ..., end_date = ...) -> Any: ...
def get_kdata_dir(item, fuquan = ...) -> str: ...
def get_report_event_date(security_item, report_period) -> Any: ...
def get_tick_dir(item) -> str: ...
def init_env() -> None: ...
def init_log() -> None: ...
def ma(security_item, start_date, end_date, level = ..., fuquan = ..., source = ..., window = ..., col = ..., return_all = ..., return_col = ...) -> Any: ...
def macd(security_item, start_date, end_date, level = ..., fuquan = ..., source = ..., slow = ..., fast = ..., n = ..., return_all = ..., return_col = ...) -> Any: ...
def mkdir_for_stock(item) -> None: ...