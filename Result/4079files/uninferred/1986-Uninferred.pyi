import foglamp.plugins.storage.common.exceptions as lib
from typing import Any

__author__: str
__copyright__: str
__license__: str
__version__: str
_MESSAGES_LIST: Any
_logger: Any
_LOG_LEVEL_DEBUG: int
_LOG_LEVEL_INFO: int
_LOGGER_LEVEL = _LOG_LEVEL_INFO
_LOGGER_DESTINATION: Any

class Backup:
    _MODULE_NAME: str = ...
    _SCHEDULE_BACKUP_ON_DEMAND: str = ...
    _MESSAGES_LIST: Any = ...
    _logger: Any = ...
    STORAGE_TABLE_BACKUPS: Any = ...
    _storage: Any = ...
    _backup_lib: Any = ...
    def __init__(self, _storage: Any) -> None: ...
    async def get_all_backups(self, limit: int, skip: int, status: [lib.BackupStatus, None], sort_order: lib.SortOrder=...) -> list: ...
    async def get_backup_details(self, backup_id: int) -> dict: ...
    async def delete_backup(self, backup_id: int) -> Any: ...
    async def _delete_backup_information(self, _id: Any) -> None: ...
    async def create_backup(self): ...
