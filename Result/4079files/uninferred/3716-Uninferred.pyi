from searchscrapeserver.common.exceptions import *
from searchscrapeserver.common.headers import random_desktop_headers as random_desktop_headers
from typing import Any

DEFAULT_YANDEX_URL: str

def build_yandex_url(geo: Any, keyword: Any, number: Any, lr: Any): ...
def unpack_data(data_dict: Any): ...
async def yandex_gather_results(data: Any): ...
