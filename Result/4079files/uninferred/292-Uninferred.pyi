from django.test import Client as Client
from typing import Any

def resp_sitemap(client: Client, db: Any) -> Any: ...
def test_sitemap_status_code(resp_sitemap: Any) -> None: ...
def resp_robots(client: Client, db: Any) -> Any: ...
def test_robots_status_code(resp_robots: Any) -> None: ...
