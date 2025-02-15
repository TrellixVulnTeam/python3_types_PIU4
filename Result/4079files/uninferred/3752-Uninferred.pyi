from pybel import BELGraph as BELGraph, Manager
from typing import Any, Iterable, List, Optional

class _Namespace:
    id: int
    def __init__(self, id: Any) -> None: ...

class DictManager(Manager):
    universe: Any = ...
    networks: Any = ...
    disease_to_id: Any = ...
    hash_to_node: Any = ...
    def __init__(self, connection: Optional[str]=...) -> None: ...
    def insert_graph(self, graph: BELGraph, **_kwargs: Any) -> Any: ...
    def get_graph_by_id(self, network_id: int) -> BELGraph: ...
    def get_graphs_by_ids(self, network_ids: Iterable[int]) -> List[BELGraph]: ...
