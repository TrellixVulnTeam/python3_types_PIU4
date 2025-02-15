# (generated with --quick)

from typing import Any, Optional, Type

datetime: Type[datetime.datetime]
defaultThrottlingOptions: ThrottlingOptions
r: module
timedelta: Type[datetime.timedelta]

class ThrottlingBucket:
    _capacity: Any
    _redis: Any
    _updated_at: Any
    base_key: Optional[str]
    cache_dict: Optional[dict]
    capacity_key: str
    options: Optional[ThrottlingOptions]
    request: None
    rule: Optional[ThrottlingRule]
    updated_at_key: str
    def __init__(self, rule: ThrottlingRule, arguments_bundle: dict, options: Optional[ThrottlingOptions] = ...) -> None: ...
    def _log(self, *msg) -> None: ...
    def check_throttle(self) -> Any: ...
    def commit_request(self) -> None: ...

class ThrottlingOptions:
    __doc__: str
    periods_to_overtake: Any
    redis: Any
    redis_instance: Any
    redis_options: Any
    verbose_mode: Any
    def __init__(self, periods_to_overtake = ..., redis_instance = ..., redis_options = ..., verbose_mode = ...) -> None: ...

class ThrottlingRule:
    __doc__: str
    cache_key: str
    interval: Any
    max_requests: Optional[int]
    def __init__(self, max_requests: int, interval) -> None: ...
    def __str__(self) -> str: ...

def build_cache_key(**arguments) -> str: ...
def localize_timedelta(delta: datetime.timedelta) -> str: ...
