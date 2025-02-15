from pyelt.datalayers.dv import *
from typing import Any, Optional

class Dim(AbstractOrderderTable):
    id: Any = ...
    _lookup_fields: Any = ...
    __dbschema__: str = ...
    @classmethod
    def cls_create_dbname(cls): ...
    @classmethod
    def cls_get_column_names_no_id(cls): ...
    @classmethod
    def cls_get_lookup_fields(cls): ...
    @classmethod
    def cls_to_pygram_dim(cls, schema_name: Any, lookup_fields: Any = ...): ...
    @classmethod
    def cls_to_pygram_bulk_dim(cls, schema_name: Any, lookup_fields: Any = ..., bulkloader: Optional[Any] = ...): ...
    @classmethod
    def cls_to_pygram_mapping(cls): ...

class Fact(AbstractOrderderTable):
    @classmethod
    def cls_create_dbname(cls): ...
    @classmethod
    def cls_get_measure_names(cls): ...
    @classmethod
    def cls_get_key_names(cls): ...
    @classmethod
    def cls_to_pygram_fact(cls, schema_name: Any): ...

class DmReference(FkReference):
    fk: Any = ...
    def __init__(self, dim_cls: Any, fk_name: str = ...) -> None: ...
