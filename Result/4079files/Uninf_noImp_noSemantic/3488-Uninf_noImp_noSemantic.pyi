import pymc3 as pm
from ..models.fancy_model import GeneralizedContinuousModel
from abc import abstractmethod
from typing import Any

class FancyStochasticOptimizer:
    @abstractmethod
    def get_optimizer(self, model: GeneralizedContinuousModel=..., approx: pm.MeanField=...) -> Any: ...
    @staticmethod
    def get_call_kwargs(_locals_: Any): ...
    @abstractmethod
    def save(self, output_path: str) -> Any: ...
    @abstractmethod
    def load(self, input_path: str) -> Any: ...

class FancyAdamax(FancyStochasticOptimizer):
    learning_rate: Any = ...
    beta1: Any = ...
    beta2: Any = ...
    epsilon: Any = ...
    sample_specific_only: Any = ...
    disable_bias_correction: Any = ...
    m_tensors: Any = ...
    u_tensors: Any = ...
    res_tensor: Any = ...
    def __init__(self, learning_rate: float=..., beta1: float=..., beta2: float=..., epsilon: float=..., sample_specific_only: bool=..., disable_bias_correction: bool=...) -> None: ...
    def _assert_shared_tensors_available(self) -> None: ...
    def get_mu_m(self): ...
    def get_rho_m(self): ...
    def get_mu_u(self): ...
    def get_rho_u(self): ...
    def get_res_tensor(self): ...
    @staticmethod
    def structured_adamax(loss_or_grads: Any=..., params: Any=..., model: GeneralizedContinuousModel=..., approx: pm.MeanField=..., learning_rate: Any=..., beta1: Any=..., beta2: Any=..., epsilon: Any=..., sample_specific_only: Any=..., disable_bias_correction: Any=..., base_class: FancyAdamax=...) -> Any: ...
    def get_optimizer(self, model: GeneralizedContinuousModel=..., approx: pm.MeanField=...) -> Any: ...
    def save(self, output_path: str) -> None: ...
    def load(self, input_path: str) -> Any: ...
    def initialize_state_from_instance(self, instance: FancyAdamax) -> Any: ...
