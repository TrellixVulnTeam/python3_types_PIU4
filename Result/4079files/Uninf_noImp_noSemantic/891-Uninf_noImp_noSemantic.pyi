def load_steam_guard(steam_guard: str) -> dict: ...
def generate_one_time_code(shared_secret: str, timestamp: int=...) -> str: ...
def generate_confirmation_key(identity_secret: str, tag: str, timestamp: int=...) -> bytes: ...
def generate_device_id(steam_id: str) -> str: ...
