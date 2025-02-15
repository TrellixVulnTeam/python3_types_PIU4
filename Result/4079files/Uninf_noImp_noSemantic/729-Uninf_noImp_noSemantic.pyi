from typing import Any

pytestmark: Any

def alltypes(con: Any): ...
def assert_sql_equal(expr: Any, expected: Any) -> None: ...
def test_aggregate_in_projection(alltypes: Any) -> None: ...
def test_add_default_order_by(alltypes: Any) -> None: ...
def test_window_frame_specs(con: Any, window: Any, frame: Any) -> None: ...
def test_cumulative_functions(alltypes: Any, cumulative: Any, static: Any) -> None: ...
def test_nested_analytic_function(alltypes: Any) -> None: ...
def test_rank_functions(alltypes: Any) -> None: ...
def test_multiple_windows(alltypes: Any) -> None: ...
def test_order_by_desc(alltypes: Any) -> None: ...
def test_row_number_does_not_require_order_by(alltypes: Any) -> None: ...
def test_row_number_properly_composes_with_arithmetic(alltypes: Any) -> None: ...
def test_unsupported_aggregate_functions(alltypes: Any, column: Any, op: Any) -> None: ...
def test_propagate_nested_windows(alltypes: Any) -> None: ...
def test_math_on_windowed_expr() -> None: ...
def test_group_by_then_different_sort_orders() -> None: ...
