# (generated with --quick)

from typing import Any

sqlite3: module

def add_user(login, pswd, email, phone, age, gender) -> Any: ...
def auth_user(login, pswd) -> Any: ...
def begin_game(login) -> Any: ...
def create_base() -> None: ...
def show_base() -> list: ...
