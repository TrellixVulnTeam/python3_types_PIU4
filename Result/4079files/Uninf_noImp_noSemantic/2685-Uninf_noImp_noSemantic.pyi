from neat import nn
from typing import Any, List

class GetCommand:
    net: Any = ...
    def __init__(self, net: nn.FeedForwardNetwork) -> None: ...
    def __call__(self, distance: int, size: int, speed: int) -> str: ...

def eval_fitness(genomes: List, config: Any) -> Any: ...
def main() -> None: ...
