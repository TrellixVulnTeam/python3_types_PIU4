from typing import Any, Optional

connection_string: str
connection_string_metrics: str

def setConnectionString(conn_string: Any) -> None: ...
def setConnectionStringForMetrics(conn_string: Any) -> None: ...
def getConnection(conn_str: Optional[Any] = ..., autocommit: bool = ...): ...
def execute(sql: Any, params: Optional[Any] = ..., statement_timeout: Optional[Any] = ..., quiet: bool = ..., conn_str: Optional[Any] = ..., on_metric_store: bool = ...): ...
def executeOnRemoteHost(sql: Any, host: Any, port: Any, dbname: Any, user: Any, password: str = ..., sslmode: str = ..., sslrootcert: str = ..., sslcert: str = ..., sslkey: str = ..., params: Optional[Any] = ..., statement_timeout: Optional[Any] = ..., quiet: bool = ...): ...
def isDataStoreConnectionOK(): ...
def isMetricStoreConnectionOK(): ...