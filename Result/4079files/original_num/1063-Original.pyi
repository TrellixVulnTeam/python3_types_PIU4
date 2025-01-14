# (generated with --quick)

from typing import Dict, Tuple

_fips_to_name_xwalk: Dict[int, str]
_name_to_fips_xwalk: Dict[str, int]
_state_abbr_to_name: Dict[str, str]
_state_name_to_abbr: Dict[str, str]
state_abbr_list: Tuple[str, ...]
state_fips_list: Tuple[int, ...]
state_names_list: Tuple[str, ...]

def state_abbr_to_fips(abbr: str) -> int: ...
def state_abbr_to_name(abbr: str) -> str: ...
def state_fips_to_abbr(fips: int) -> str: ...
def state_fips_to_name(fips: int) -> str: ...
def state_name_to_abbr(name: str) -> str: ...
def state_name_to_fips(name: str) -> int: ...
