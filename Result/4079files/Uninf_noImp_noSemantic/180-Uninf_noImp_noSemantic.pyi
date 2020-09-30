from typing import Any, Optional

class PWEVisualization:
    @staticmethod
    def dbscan_clustering(dist_matrix: Any, save_to_file: Optional[Any] = ...): ...
    @staticmethod
    def linkage_dendrogram(dist_matrix: Any, pws_used: list=..., save_to_folder: Any=...) -> Any: ...
    @staticmethod
    def mds_networkx(pws_used: Any, A: Any, scale_down_factor: Any, save_to_file: bool = ...): ...
    @staticmethod
    def mds_sklearn(A: Any, save_to_file: Optional[Any] = ...): ...
    @staticmethod
    def graphviz_from_meta_data(pw_rel_dfs: Any, graphviz_meta_data: Any): ...
    @staticmethod
    def cluster_map_viz(dist_matrix: Any, pw_ids: list=..., cmap: Any=...) -> Any: ...