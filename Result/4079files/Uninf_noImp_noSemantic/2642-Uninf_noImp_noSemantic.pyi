from sklearn.base import BaseEstimator
from typing import Any, Optional

class EnsembleClassifier(BaseEstimator):
    estimator: Any = ...
    n_jobs: Any = ...
    n_runs: Any = ...
    alpha: Any = ...
    seed: Any = ...
    warmup: Any = ...
    memory: Any = ...
    def __init__(self, estimator: Any, n_jobs: int = ..., seed: Optional[Any] = ..., n_runs: int = ..., alpha: float = ..., memory: Any = ..., warmup: bool = ...) -> None: ...
    estimator_: Any = ...
    def fit(self, X: Any, y: Any, callback: Optional[Any] = ...): ...
    def predict(self, X: Any): ...

def _compute_coefs(estimator: Any, X: Any, y: Any, seed: int = ...): ...
def _compute_components(embedder_weights: Any, embedder_init: Any, alpha: Any, warmup: Any): ...
