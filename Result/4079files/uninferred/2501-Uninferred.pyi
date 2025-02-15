from neuralmonkey.runners.base_runner import BaseRunner, Executable, NextExecute as NextExecute
from typing import Any, Callable, Dict, List

class LabelRunner(BaseRunner):
    _postprocess: Any = ...
    def __init__(self, output_series: str, decoder: Any, postprocess: Callable[[List[str]], List[str]]=...) -> None: ...
    def get_executable(self, compute_losses: bool = ..., summaries: bool = ...): ...
    @property
    def loss_names(self) -> List[str]: ...

class LabelRunExecutable(Executable):
    all_coders: Any = ...
    _fetches: Any = ...
    _vocabulary: Any = ...
    _postprocess: Any = ...
    decoded_labels: Any = ...
    result: Any = ...
    def __init__(self, all_coders: Any, fetches: Any, vocabulary: Any, postprocess: Any) -> None: ...
    def next_to_execute(self) -> NextExecute: ...
    def collect_results(self, results: List[Dict]) -> None: ...
