from irisett import object_models
from irisett.sql import DBConnection
from typing import Any, Dict, Iterable, Optional

async def get_metadata(dbcon: DBConnection, object_type: str, object_id: int) -> Dict[str, str]: ...
async def add_metadata(dbcon: DBConnection, object_type: str, object_id: int, metadict: Dict[str, str]) -> Any: ...
async def update_metadata(dbcon: DBConnection, object_type: str, object_id: int, metadict: Dict[str, str]) -> Any: ...
async def delete_metadata(dbcon: DBConnection, object_type: str, object_id: int, keys: Optional[Iterable[str]]=...) -> Any: ...
async def get_metadata_for_object(dbcon: DBConnection, object_type: str, object_id: int) -> Iterable[object_models.ObjectMetadata]: ...
async def get_metadata_for_object_type(dbcon: DBConnection, object_type: str) -> Iterable[object_models.ObjectMetadata]: ...
async def get_metadata_for_object_metadata(dbcon: DBConnection, metadata_key: str, metadata_value: str, object_type: str, object_table: str) -> Iterable[object_models.ObjectMetadata]: ...
