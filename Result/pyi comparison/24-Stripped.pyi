# (generated with --quick)

from typing import Any, List

__package__: None
locations: Any
logger: logging.Logger
logging: module
operator: module
sys: module
verboselogs: Any

def filter_by_area(area, type_country_filtered) -> list: ...
def filter_by_country(country_code, type_filtered_servers) -> list: ...
def filter_by_load(server_list, max_load, top_servers) -> list: ...
def filter_by_location(location, type_filtered_servers) -> list: ...
def filter_by_protocol(json_res_list, tcp) -> List[list]: ...
def filter_by_type(json_response, p2p, dedicated, double_vpn, tor_over_vpn, anti_ddos, netflix) -> list: ...