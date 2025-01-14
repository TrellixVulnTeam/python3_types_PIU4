import tweepy
from discord.ext import commands
from typing import Any, Optional

errors_logger: Any

def setup(bot: Any) -> None: ...

class TwitterStreamListener(tweepy.StreamListener):
    bot: Any = ...
    blacklisted_handles: Any = ...
    stream: Any = ...
    feeds: Any = ...
    unique_feeds: Any = ...
    reconnect_ready: Any = ...
    reconnecting: bool = ...
    def __init__(self, bot: Any, blacklisted_handles: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...
    async def start_feeds(self, *, feeds: Optional[Any] = ...): ...
    async def add_feed(self, channel: Any, handle: Any) -> None: ...
    async def remove_feed(self, channel: Any, handle: Any) -> None: ...
    def on_status(self, status: Any) -> None: ...
    def on_error(self, status_code: Any): ...
    def on_exception(self, exception: Any) -> None: ...

class Twitter(commands.Cog):
    bot: Any = ...
    blacklisted_handles: Any = ...
    stream_listener: Any = ...
    task: Any = ...
    def __init__(self, bot: Any) -> None: ...
    def cog_unload(self) -> None: ...
    async def initialize_database(self) -> None: ...
    async def twitter(self, ctx: Any) -> None: ...
    async def twitter_status(self, ctx: Any, handle: str, replies: bool=..., retweets: bool=...) -> Any: ...
    async def twitter_add(self, ctx: Any, handle: str) -> Any: ...
    async def twitter_remove(self, ctx: Any, handle: str) -> Any: ...
    async def handles(self, ctx: Any) -> None: ...
    def process_tweet_text(self, text: Any, entities: Any): ...
    async def start_twitter_feeds(self) -> None: ...
