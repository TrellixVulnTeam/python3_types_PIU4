# (generated with --quick)

from typing import Any, Iterator

Doc2Vec: Any
TaggedDocument: Any
pickle: module

class Doc2VecModel:
    _model: Any
    _preprocessor: Any
    def __init__(self, preprocessor) -> None: ...
    def find_neighbors(self, vec) -> Any: ...
    def infer_vector(self, text: str) -> Any: ...
    def save(self, path: str) -> None: ...
    def train(self, train_docs: Iterator[str]) -> None: ...

def infer(model, document) -> None: ...
def load(path: str) -> Any: ...
