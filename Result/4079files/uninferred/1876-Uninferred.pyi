from typing import Any

class s3_scanner:
    host: Any = ...
    results: str = ...
    totalresults: str = ...
    fingerprints: Any = ...
    def __init__(self, host: Any) -> None: ...
    def __check_http(self, bucket_url: Any) -> None: ...
    temp: Any = ...
    def do_s3(self) -> None: ...
    def process(self) -> None: ...
