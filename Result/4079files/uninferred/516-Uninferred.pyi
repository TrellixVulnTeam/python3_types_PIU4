from typing import Any

def test_schema(schema_func_name: Any, args_qty: Any) -> None: ...
def test_query(query_func_name: Any, args_qty: Any) -> None: ...
def test_changefeed(changefeed_func_name: Any, args_qty: Any) -> None: ...
def test_changefeed_class(changefeed_class_func_name: Any, args_qty: Any) -> None: ...
def test_admin(admin_func_name: Any, kwargs: Any) -> None: ...
