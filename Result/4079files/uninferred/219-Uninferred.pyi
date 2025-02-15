from typing import Any

class TutorialSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler: Any): ...
    def process_spider_input(response: Any, spider: Any) -> None: ...
    def process_spider_output(response: Any, result: Any, spider: Any) -> None: ...
    def process_spider_exception(response: Any, exception: Any, spider: Any) -> None: ...
    def process_start_requests(start_requests: Any, spider: Any) -> None: ...
    def spider_opened(self, spider: Any) -> None: ...
