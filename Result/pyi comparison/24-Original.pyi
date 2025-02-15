# (generated with --quick)

from typing import Any

__package__: None
locations: Any
logger: logging.Logger
logging: module
operator: module
sys: module
verboselogs: Any

def filter_by_area(area: str, type_country_filtered: list) -> list: ...
def filter_by_country(country_code: str, type_filtered_servers: list) -> list: ...
def filter_by_load(server_list: list, max_load: int, top_servers: int) -> list: ...
def filter_by_location(location: float, type_filtered_servers: list) -> list: ...
def filter_by_protocol(json_res_list: list, tcp: bool) -> list: ...
def filter_by_type(json_response, p2p: bool, dedicated: bool, double_vpn: bool, tor_over_vpn: bool, anti_ddos: bool, netflix: bool) -> list: ...
