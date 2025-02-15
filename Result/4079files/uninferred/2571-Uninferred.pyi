from typing import Any

log: Any

class Database:
    pool: Any = ...
    sql: Any = ...
    def __init__(self, pool: Any) -> None: ...
    @staticmethod
    async def create_database(loop: Any, username: Any, password: Any, database: Any, *, hostname: str = ..., port: int = ...): ...
    async def close(self) -> None: ...
    async def add_subscription(self, subscriber_id: int, service: str, username: str, service_id: str) -> Any: ...
    async def del_subscription(self, subscriber_id: int, service: str, username: str) -> Any: ...
    async def delete_subscriber(self, subscriber_id: int) -> Any: ...
    async def get_all_streamers_from_service(self, service: str) -> Any: ...
    async def get_subscribers_from_streamer(self, streamer_id: str) -> Any: ...
    async def get_subscriptions_from_subscriber(self, subscriber_id: int, service: str) -> Any: ...
