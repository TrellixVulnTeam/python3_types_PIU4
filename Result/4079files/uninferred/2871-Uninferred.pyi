from homeassistant.helpers.entity import Entity
from typing import Any, Optional

_LOGGER: Any
DEFAULT_NAME: str
ICON: str

async def async_setup_platform(hass: Any, config: Any, async_add_entities: Any, discovery_info: Optional[Any] = ...) -> None: ...

class UptimeSensor(Entity):
    _name: Any = ...
    _unit: Any = ...
    initial: Any = ...
    _state: Any = ...
    def __init__(self, name: Any, unit: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def icon(self): ...
    @property
    def unit_of_measurement(self): ...
    @property
    def state(self): ...
    async def async_update(self) -> None: ...
