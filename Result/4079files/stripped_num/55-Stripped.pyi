# (generated with --quick)

import sqlite3.dbapi2
from typing import Any, List, Optional, Tuple, Type

DBConnector: Any
QTemporaryFile: Any
QUrl: Any
QgsCoordinateReferenceSystem: Any
QgsDataSourceUri: Any
QgsMapLayerType: Any
QgsProject: Any
QgsVectorLayer: Any
QgsVirtualLayerDefinition: Any
QgsWkbTypes: Any
Table: Any
sqlite3: module

class VLayerConnector(Any):
    def __init__(self, uri) -> None: ...
    def _execute(self, cursor, sql) -> Any: ...
    def _get_cursor(self, name = ...) -> None: ...
    def _get_cursor_columns(self, c) -> list: ...
    def addGeometryColumn(self, table, geom_column = ..., geom_type = ..., srid = ..., dim = ...) -> bool: ...
    def addTableColumn(self, table, field_def) -> bool: ...
    def addTablePrimaryKey(self, table, column) -> bool: ...
    def addTableUniqueConstraint(self, table, column) -> bool: ...
    def connection_error_types(self) -> bool: ...
    def createSpatialIndex(self, table, geom_column = ...) -> bool: ...
    def createTable(self, table, field_defs, pkey) -> bool: ...
    def createTableIndex(self, table, name, column, unique = ...) -> bool: ...
    def createView(self, view, query) -> bool: ...
    def deleteGeometryColumn(self, table, geom_column) -> bool: ...
    def deleteSpatialIndex(self, table, geom_column = ...) -> bool: ...
    def deleteTable(self, table) -> bool: ...
    def deleteTableColumn(self, table, column) -> None: ...
    def deleteTableConstraint(self, table, constraint) -> bool: ...
    def deleteTableIndex(self, table, name) -> bool: ...
    def deleteTableTrigger(self, trigger, table = ...) -> None: ...
    def deleteView(self, view) -> bool: ...
    def emptyTable(self, table) -> bool: ...
    def execution_error_types(self) -> bool: ...
    def fieldTypes(self) -> List[str]: ...
    def getInfo(self) -> str: ...
    def getQueryBuilderDictionary(self) -> Any: ...
    def getRasterTables(self, schema = ...) -> List[nothing]: ...
    def getSchemas(self) -> None: ...
    def getSpatialInfo(self) -> None: ...
    def getSpatialRefInfo(self, srid) -> Any: ...
    def getSqlDictionary(self) -> Any: ...
    def getTableConstraints(self, table) -> None: ...
    def getTableExtent(self, table, geom) -> Optional[Tuple[Any, Any, Any, Any]]: ...
    def getTableFields(self, table) -> List[Tuple[Any, Any, Any, bool, None, bool]]: ...
    def getTableIndexes(self, table) -> List[nothing]: ...
    def getTableRowCount(self, table) -> Any: ...
    def getTableTriggers(self, table) -> List[nothing]: ...
    def getTables(self, schema = ..., add_sys_tables = ...) -> List[Tuple[Any, Any, bool, bool, Any, str, Optional[str], Optional[str], Any]]: ...
    def getVectorTables(self, schema = ...) -> List[Tuple[Any, Any, bool, bool, Any, str, Optional[str], Optional[str], Any]]: ...
    def getViewDefinition(self, view) -> None: ...
    def hasCustomQuerySupport(self) -> bool: ...
    def hasRasterSupport(self) -> bool: ...
    def hasSpatialIndex(self, table, geom_column = ...) -> bool: ...
    def hasSpatialSupport(self) -> bool: ...
    def hasTableColumnEditingSupport(self) -> bool: ...
    def isGeometryColumn(self, table, column) -> bool: ...
    def isRasterTable(self, table) -> bool: ...
    def isVectorTable(self, table) -> bool: ...
    def moveTable(self, table, new_table, new_schema = ...) -> bool: ...
    def renameTable(self, table, new_table) -> bool: ...
    def renameTableColumn(self, table, column, new_name) -> bool: ...
    def renameView(self, view, new_name) -> bool: ...
    def runVacuum(self) -> bool: ...
    def setColumnDefault(self, table, column, default) -> bool: ...
    def setColumnNull(self, table, column, is_null) -> bool: ...
    def setColumnType(self, table, column, data_type) -> bool: ...
    def updateTableColumn(self, table, column, new_name, new_data_type = ..., new_not_null = ..., new_default = ..., comment = ...) -> None: ...
    def uri(self) -> Any: ...

class VLayerRegistry(object):
    _instance: Optional[VLayerRegistry]
    layers: dict
    def __getitem__(self, k) -> None: ...
    def __setitem__(self, k, l) -> None: ...
    def get(self, k) -> Any: ...
    def getLayer(self, l) -> Any: ...
    def has(self, k) -> bool: ...
    @classmethod
    def instance(cls) -> Any: ...
    def items(self) -> List[Tuple[Any, Any]]: ...
    def reset(self) -> None: ...
    def set(self, k, l) -> None: ...

class sqlite3_connection(object):
    conn: sqlite3.dbapi2.Connection
    def __enter__(self) -> sqlite3.dbapi2.Connection: ...
    def __exit__(self, type, value, traceback) -> None: ...
    def __init__(self, sqlite_file) -> None: ...

def classFactory() -> Type[VLayerConnector]: ...
def getQueryGeometryName(sqlite_file) -> Any: ...