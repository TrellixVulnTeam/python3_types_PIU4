# (generated with --quick)

from typing import Any, NoReturn, Tuple

PW_CHANGE: int
PW_NEW: int
PW_PASSPHRASE: int
Qt: Any
_: Any
math: module
re: module
run_hook: Any

class ChangePasswordDialogBase(Any):
    def __init__(self, parent, wallet) -> NoReturn: ...
    def create_password_layout(self, wallet, is_encrypted, OK_button) -> NoReturn: ...

class ChangePasswordDialogForHW(ChangePasswordDialogBase):
    playout: PasswordLayoutForHW
    def __init__(self, parent, wallet) -> None: ...
    def create_password_layout(self, wallet, is_encrypted, OK_button) -> None: ...
    def run(self) -> Tuple[bool, Any]: ...

class ChangePasswordDialogForSW(ChangePasswordDialogBase):
    playout: PasswordLayout
    def __init__(self, parent, wallet) -> None: ...
    def create_password_layout(self, wallet, is_encrypted, OK_button) -> None: ...
    def run(self) -> Tuple[bool, Any, Any, Any]: ...

class PasswordDialog(Any):
    pw: Any
    def __init__(self, parent = ..., msg = ...) -> None: ...
    def run(self) -> Any: ...

class PasswordLayout(object):
    OK_button: Any
    conf_pw: Any
    encrypt_cb: Any
    kind: Any
    new_pw: Any
    pw: Any
    pw_strength: Any
    titles: list
    vbox: Any
    wallet: Any
    def __init__(self, wallet, msg, kind, OK_button, force_disable_encrypt_cb = ...) -> None: ...
    def layout(self) -> Any: ...
    def new_password(self) -> Any: ...
    def old_password(self) -> Any: ...
    def pw_changed(self) -> None: ...
    def title(self) -> Any: ...

class PasswordLayoutForHW(object):
    OK_button: Any
    encrypt_cb: Any
    kind: Any
    vbox: Any
    wallet: Any
    def __init__(self, wallet, msg, kind, OK_button) -> None: ...
    def layout(self) -> Any: ...
    def title(self) -> Any: ...

def __getattr__(name) -> Any: ...
def check_password_strength(password) -> str: ...
