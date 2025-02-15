# (generated with --quick)

from typing import Any, Tuple

np: module

class HMMEstimator(object):
    __doc__: str
    error: Any
    n_iter: Any
    n_states: Any
    obprob: Any
    startprob: Any
    transmat: Any
    def __init__(self, transmat = ..., obprob = ..., startprob = ..., n_states = ..., n_iter = ..., error = ...) -> None: ...
    def _backward(self, seq) -> Any: ...
    def _forward(self, seq) -> Any: ...
    def _gamma(self, seq) -> Any: ...
    def _xi(self, seq) -> Any: ...
    def backward_prob(self, seq) -> Any: ...
    def decoding(self, seq) -> Tuple[Any, Any]: ...
    def fit(self, seq) -> None: ...
    def forward_prob(self, seq) -> Any: ...
    def predict(self, seq) -> None: ...
    def score(self, seq, method = ...) -> Any: ...
