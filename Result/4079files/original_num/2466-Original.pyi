# (generated with --quick)

from typing import Any, Dict, Iterable, List

C: Any
argparse: module
arguments: Any
itertools: module
log_sockeye_version: Any
logger: logging.Logger
logging: module
mx: Any
os: module
setup_main_logger: Any
utils: Any

def _strategy_best(points, size, maximize) -> list: ...
def _strategy_last(points, size, maximize) -> Any: ...
def _strategy_lifespan(points, size, maximize) -> List[List[nothing]]: ...
def average(param_paths: Iterable[str]) -> Dict[str, Any]: ...
def average_parameters(args: argparse.Namespace) -> None: ...
def find_checkpoints(model_path: str, size = ..., strategy = ..., metric: str = ...) -> List[str]: ...
def main() -> None: ...
