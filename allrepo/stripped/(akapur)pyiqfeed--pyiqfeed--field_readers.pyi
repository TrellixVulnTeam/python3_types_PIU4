# (generated with --quick)

from typing import Any, Tuple

UnexpectedField: Any
datetime: module
np: module

def blob_to_str(val) -> str: ...
def date_to_yyyymmdd(dt) -> str: ...
def date_us_to_datetime(dt64, tm_int) -> datetime.datetime: ...
def datetime64_to_date(dt64) -> Any: ...
def datetime_to_yyyymmdd_hhmmss(dt_tm) -> str: ...
def read_ccyymmdd(field) -> Any: ...
def read_float(field) -> float: ...
def read_float64(field) -> Any: ...
def read_hex(field) -> int: ...
def read_hhmmss(field) -> int: ...
def read_hhmmss_no_colon(field) -> int: ...
def read_hhmmssmil(field) -> int: ...
def read_hhmmssus(field) -> int: ...
def read_hist_news_timestamp(dt_tm) -> Tuple[Any, int]: ...
def read_int(field) -> int: ...
def read_is_market_open(field) -> bool: ...
def read_is_short_restricted(field) -> bool: ...
def read_live_news_timestamp(dt_tm) -> Tuple[Any, int]: ...
def read_mmddccyy(field) -> Any: ...
def read_posix_ts(dt_tm_str) -> Tuple[Any, int]: ...
def read_posix_ts_mil(dt_tm_str) -> Tuple[Any, int]: ...
def read_posix_ts_us(dt_tm_str) -> Tuple[Any, int]: ...
def read_split_string(split_str) -> Tuple[Any, Any]: ...
def read_tick_direction(field) -> Any: ...
def read_timestamp_msg(dt_tm) -> Tuple[Any, int]: ...
def read_uint16(field) -> Any: ...
def read_uint64(field) -> Any: ...
def read_uint8(field) -> Any: ...
def str_or_blank(val) -> str: ...
def time_to_hhmmss(tm) -> str: ...
def us_since_midnight_to_time(us_dt) -> datetime.time: ...