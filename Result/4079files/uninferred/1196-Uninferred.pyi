from pybel import BELGraph
from typing import Any, Iterable, Mapping, Optional

def get_merged_namespace_names(locations: Iterable[str], check_keywords: bool=...) -> Mapping[str, str]: ...
def merge_namespaces(input_locations: Any, output_path: Any, namespace_name: Any, namespace_keyword: Any, namespace_domain: Any, author_name: Any, citation_name: Any, namespace_description: Any=..., namespace_species: Any=..., namespace_version: Any=..., namespace_query_url: Any=..., namespace_created: Any=..., author_contact: Any=..., author_copyright: Any=..., citation_description: Any=..., citation_url: Any=..., citation_version: Any=..., citation_date: Any=..., case_sensitive: Any=..., delimiter: Any=..., cacheable: Any=..., check_keywords: Any=...) -> None: ...
def export_namespace(graph: BELGraph, namespace: str, directory: Optional[str]=..., cacheable: bool=...) -> None: ...
def export_namespaces(graph: BELGraph, namespaces: Iterable[str], directory: Optional[str]=..., cacheable: bool=...) -> None: ...
