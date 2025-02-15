# (generated with --quick)

import collections
import functools
from typing import Any, Callable, NoReturn, Optional, Type, TypeVar, Union

GeneralizedContinuousModel: Any
OrderedDict: Type[collections.OrderedDict]
get_or_compute_grads: Any
io_commons: Any
np: module
partial: Type[functools.partial]
pm: Any
th: Any
tt: Any
types: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class FancyAdamax(FancyStochasticOptimizer):
    __doc__: str
    beta1: float
    beta2: float
    disable_bias_correction: bool
    epsilon: float
    learning_rate: float
    m_tensors: list
    res_tensor: Any
    sample_specific_only: bool
    u_tensors: list
    def __init__(self, learning_rate: float = ..., beta1: float = ..., beta2: float = ..., epsilon: float = ..., sample_specific_only: bool = ..., disable_bias_correction: bool = ...) -> None: ...
    def _assert_shared_tensors_available(self) -> None: ...
    def get_mu_m(self) -> Any: ...
    def get_mu_u(self) -> Any: ...
    def get_optimizer(self, model = ..., approx = ...) -> functools.partial[nothing]: ...
    def get_res_tensor(self) -> Any: ...
    def get_rho_m(self) -> Any: ...
    def get_rho_u(self) -> Any: ...
    def initialize_state_from_instance(self, instance: FancyAdamax) -> None: ...
    def load(self, input_path: str) -> None: ...
    def save(self, output_path: str) -> None: ...
    @staticmethod
    def structured_adamax(loss_or_grads = ..., params = ..., model = ..., approx = ..., learning_rate = ..., beta1 = ..., beta2 = ..., epsilon = ..., sample_specific_only = ..., disable_bias_correction = ..., base_class: Optional[FancyAdamax] = ...) -> Union[collections.OrderedDict, functools.partial[nothing]]: ...

class FancyStochasticOptimizer:
    __doc__: str
    @staticmethod
    def get_call_kwargs(_locals_) -> Any: ...
    @abstractmethod
    def get_optimizer(self, model = ..., approx = ...) -> NoReturn: ...
    @abstractmethod
    def load(self, input_path: str) -> NoReturn: ...
    @abstractmethod
    def save(self, output_path: str) -> NoReturn: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
