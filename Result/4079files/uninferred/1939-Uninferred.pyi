from typing import Any

def check_credentials(username: Any, pw: Any): ...
def not_authorized(): ...
def requires_auth(func: Any): ...
