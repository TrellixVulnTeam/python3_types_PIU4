import requests
from typing import Any

logger: Any

class Authentication:
    def is_ready(self) -> bool: ...
    def get_session(self) -> requests.Session: ...

class TokenAuthentication(Authentication):
    auth_token: Any = ...
    def __init__(self, auth_token: str=...) -> None: ...
    def set_token(self, auth_token: str) -> Any: ...
    def is_ready(self) -> bool: ...
    def get_session(self) -> requests.Session: ...

class OAuthAuthentication(Authentication):
    base_url: str = ...
    auth_url: str = ...
    token_url: str = ...
    redirect_url: Any = ...
    client_id: Any = ...
    client_secret: Any = ...
    real_auth: Any = ...
    def __init__(self, redirect_url: str, client_id: str, client_secret: str, auth_token: str=...) -> None: ...
    def authorize_url(self, scope: list, state: str=...) -> tuple: ...
    def obtain_token(self, redirect_url: str, state: str) -> str: ...
    def is_ready(self) -> bool: ...
    def get_session(self) -> requests.Session: ...
    @staticmethod
    def _generate_state() -> str: ...
    class OAuthError(Exception):
        error_code: Any = ...
        def __init__(self, error_code: str, description: str=...) -> None: ...