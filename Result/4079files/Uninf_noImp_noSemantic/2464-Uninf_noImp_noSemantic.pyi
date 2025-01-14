from .red_base import BaseDriver, IdentifierData
from pathlib import Path
from typing import Any, Dict

__all__: Any
_shared_datastore: Any
_driver_counts: Any
_finalizers: Any
log: Any

def finalize_driver(cog_name: Any) -> None: ...

class JSON(BaseDriver):
    file_name: Any = ...
    data_path: Any = ...
    _lock: Any = ...
    def __init__(self, cog_name: Any, identifier: Any, *, data_path_override: Path=..., file_name_override: str=...) -> None: ...
    async def has_valid_connection(self) -> bool: ...
    @property
    def data(self): ...
    @data.setter
    def data(self, value: Any) -> None: ...
    def _load_data(self) -> None: ...
    def migrate_identifier(self, raw_identifier: int) -> Any: ...
    async def get(self, identifier_data: IdentifierData) -> Any: ...
    async def set(self, identifier_data: IdentifierData, value: Any=...) -> Any: ...
    async def clear(self, identifier_data: IdentifierData) -> Any: ...
    async def import_data(self, cog_data: Any, custom_group_data: Any) -> None: ...
    async def _save(self) -> None: ...
    def get_config_details(self) -> None: ...

def _save_json(path: Path, data: Dict[str, Any]) -> None: ...
