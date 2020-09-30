from typing import Any, Optional

class Strategy:
    broker: Any = ...
    current_date: Any = ...
    commission: Any = ...
    margin: Any = ...
    queue: Any = ...
    order_list: Any = ...
    start_date: Any = ...
    end_date: Any = ...
    sizer: Any = ...
    tradable: bool = ...
    def __init__(self, broker: Any, queue: Any, comm_func: Any, margin_func: Any, **params: Any) -> None: ...
    def positions_total(self): ...
    def set_cash(self, amt: Any) -> None: ...
    def add_option(self, symbol: Any, exclude_splits: bool = ..., option_type: Optional[Any] = ...) -> None: ...
    def set_start_date(self, year: Any, month: Any, day: Any) -> None: ...
    def set_end_date(self, year: Any, month: Any, day: Any) -> None: ...
    def _init(self, **params: Any) -> None: ...
    def on_init(self, **params: Any) -> None: ...
    def on_data_event(self, event: Any) -> None: ...
    def on_data(self, data: Any) -> None: ...
    def on_fill_event(self, event: Any) -> None: ...
    def on_fill(self, event: Any) -> None: ...
    def on_rejected_event(self, event: Any) -> None: ...
    def on_rejected(self, event: Any) -> None: ...
    def place_order(self, strategy: Any, action: Any, quantity: Optional[Any] = ..., order_tif: Any = ..., order_type: Any = ..., limit_price: Optional[Any] = ...) -> None: ...
    def close_order(self, ticket: Any, price: Optional[Any] = ...) -> None: ...
    def cancel(self) -> None: ...