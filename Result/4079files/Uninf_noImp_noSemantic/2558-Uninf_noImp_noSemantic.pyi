from sqlalchemy import engine_from_config as engine_from_config
from typing import Any

config: Any
target_metadata: Any

def get_database_url(): ...
def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
