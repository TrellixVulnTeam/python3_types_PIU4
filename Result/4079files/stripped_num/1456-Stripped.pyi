# (generated with --quick)

from typing import Any, Dict, List

pipette: Any
placeable: Any

def _get_all_containers(robot) -> list: ...
def are_instrument_positions_calibrated(instrument) -> bool: ...
def get_all_pipettes(robot) -> list: ...
def get_state(robot) -> List[Dict[str, Any]]: ...
def get_unique_containers(instrument) -> list: ...
def is_inst_calibrated_to_container(instrument, container) -> bool: ...
def sort_containers(container_list) -> list: ...
