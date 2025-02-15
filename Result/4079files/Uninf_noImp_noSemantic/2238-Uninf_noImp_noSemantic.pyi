from chainer import Chain, Variable
from rtype import State
from typing import Any, List, Tuple

Classifier: Any

class LSTM(Chain):
    embed_dim: Any = ...
    n_units: Any = ...
    gpu: Any = ...
    def __init__(self, embed_dim: int, n_units: int=..., gpu: int=...) -> None: ...
    def set_word_embedding(self, array: Any) -> None: ...
    def reset_state(self) -> None: ...
    def forward_one(self, word: Variable, state: State, dropout: bool=..., train: bool=...) -> Tuple[Variable, State]: ...
    def forward(self, words: List[Variable], state: State, dropout: bool=..., train: bool=...) -> Tuple[List[Variable], State]: ...
    def __call__(self, words: List[Variable], state: State, dropout: bool=..., train: bool=...) -> Any: ...
