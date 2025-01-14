import aiohttp
from typing import Any

class WeatherStationInfo:
    required_fields: Any = ...
    station_name: Any = ...
    station_id: Any = ...
    road_temp: Any = ...
    air_temp: Any = ...
    humidity: Any = ...
    precipitationtype: Any = ...
    winddirection: Any = ...
    winddirectiontext: Any = ...
    windforce: Any = ...
    def __init__(self, station_name: str, station_id: str, road_temp: float, air_temp: float, humidity: float, precipitationtype: str, winddirection: float, winddirectiontext: str, windforce: float) -> None: ...
    @classmethod
    def from_xml_node(cls, node: Any): ...

class TrafikverketWeather:
    _api: Any = ...
    def __init__(self, client_session: aiohttp.ClientSession, api_key: str) -> None: ...
    async def async_get_weather(self, location_name: str) -> WeatherStationInfo: ...
