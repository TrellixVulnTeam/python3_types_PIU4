from abc import ABCMeta, abstractmethod
from asphalt.core.context import Context
from typing import Any, Dict, Optional, Union

__all__: Any

class Component(metaclass=ABCMeta):
    __slots__: Any = ...
    @abstractmethod
    async def start(self, ctx: Context) -> Any: ...

class ContainerComponent(Component):
    __slots__: Any = ...
    child_components: Any = ...
    component_configs: Any = ...
    def __init__(self, components: Dict[str, Optional[Dict[str, Any]]]=...) -> None: ...
    def add_component(self, alias: str, type: Union[str, type]=..., **config: Any) -> Any: ...
    async def start(self, ctx: Context) -> Any: ...

class CLIApplicationComponent(ContainerComponent):
    async def start(self, ctx: Context) -> Any: ...
    @abstractmethod
    async def run(self, ctx: Context) -> Optional[int]: ...

component_types: Any
