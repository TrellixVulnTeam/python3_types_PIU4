from ai.STA.Strategy.strategy import Strategy as Strategy
from typing import Any, Dict, List, Type

__author__: str

class StrategyBook:
    logger: Any = ...
    stop_strategy: Any = ...
    default_strategies: Any = ...
    strategy_book: Any = ...
    def __init__(self) -> None: ...
    @property
    def strategies_name(self) -> List[str]: ...
    @property
    def strategies_roles(self) -> Dict[str, Dict[str, List[str]]]: ...
    def get_strategy(self, strategy_name: str) -> Type[Strategy]: ...
    def check_existance_strategy(self, strategy_name: str) -> bool: ...
