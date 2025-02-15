# (generated with --quick)

from typing import Any, Dict, Generator, List, TypeVar

Stats: Any
__author__: str
__copyright__: str
__credits__: List[str]
__email__: str
__license__: str
__maintainer__: str
__status__: str
__version__: str
ensemble: Any
pydotplus: Any
tree: Any

PandasDataFrame = TypeVar('PandasDataFrame')
SklearnRandomForestClassifier = TypeVar('SklearnRandomForestClassifier')

class _RandomForestClassifier(Any):
    def __init__(self) -> None: ...
    def plot(self, model_train, feature_names, class_names = ...) -> Generator[Any, Any, None]: ...
    def train(self, features_indep_df, feature_target, model_labals = ..., **kwargs) -> Any: ...
    def train_summaries(self, model_train) -> Dict[str, Any]: ...
