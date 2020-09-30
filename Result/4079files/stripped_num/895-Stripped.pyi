# (generated with --quick)

import contextlib
from typing import Any, Callable, Coroutine, Pattern, Type
import utils.formatting
import utils.time

EMOJI_RE: Pattern[str]
FORMATTING_RE: Pattern[str]
MENTION_RE: Pattern[str]
NUMERIC_RE: Pattern[str]
Table: Type[utils.formatting.Table]
Timer: Type[utils.time.Timer]
asyncio: module
discord: Any
re: module
setup_logging: Callable[..., contextlib._GeneratorContextManager]

def clean_accents(text) -> Any: ...
def clean_codeblock(text) -> Any: ...
def clean_formatting(text) -> str: ...
def clean_text(text, guild) -> Any: ...
def get_json(url, *, session = ..., **kwargs) -> coroutine: ...
def haste(content, *, session = ...) -> Coroutine[Any, Any, str]: ...
def human_delta(delta, *, short = ...) -> str: ...
def shell(command) -> Coroutine[Any, Any, str]: ...
def transform_mentions(text, guild) -> str: ...
def unique(iterable) -> list: ...