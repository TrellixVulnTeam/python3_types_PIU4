from daft import Node, PGM as PGM
from typing import Any, List

app: Any

def static_file(path: Any): ...
def render(): ...

class GraphGenerationHelpers:
    def layer(self, graph: PGM, node_texts: List[str], x: float, y: float, spacing: float=..., spacing_pow: float=..., **other_node_params: Any) -> List[Node]: ...
    def fully_connect(self, graph: PGM, layer1: List[Node], layer2: List[Node]) -> Any: ...
    def add_label(self, graph: PGM, text: str, x: float, y: float, label_id: str=..., color: str=..., size: str=..., weight: str=...) -> Any: ...
    def add_label_range(self, graph: PGM, labels: List[str], x: float, y: float, spacing: float=..., spacing_exp: float=..., direction: str=..., overrides: dict=..., **other_label_args: Any) -> Any: ...
