# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

Meld: Any
re: module

class TenhouDecoder(object):
    RANKS: List[str]
    def generate_auth_token(self, auth_string) -> Any: ...
    def get_attribute_content(self, message, attribute_name) -> Any: ...
    def get_enemy_seat(self, message) -> int: ...
    def is_discarded_tile_message(self, message) -> bool: ...
    def is_opened_set_message(self, message) -> bool: ...
    def parse_chi(self, data, meld) -> None: ...
    def parse_dora_indicator(self, message) -> int: ...
    def parse_final_scores_and_uma(self, message) -> Dict[str, List[float]]: ...
    def parse_go_tag(self, message) -> int: ...
    def parse_hello_string(self, message) -> Tuple[Any, Any, str]: ...
    def parse_initial_hand(self, message) -> List[int]: ...
    def parse_initial_values(self, message) -> Dict[str, Union[int, List[int]]]: ...
    def parse_kan(self, data, meld) -> None: ...
    def parse_log_link(self, message) -> Tuple[Any, int]: ...
    def parse_meld(self, message) -> Any: ...
    def parse_names_and_ranks(self, message) -> List[Dict[str, str]]: ...
    def parse_nuki(self, data, meld) -> None: ...
    def parse_pon(self, data, meld) -> None: ...
    def parse_table_state_after_reconnection(self, message) -> List[Dict[str, list]]: ...
    def parse_tile(self, message) -> int: ...
    def parse_who_called_riichi(self, message) -> int: ...

def unquote(string: str, encoding: str = ..., errors: str = ...) -> str: ...