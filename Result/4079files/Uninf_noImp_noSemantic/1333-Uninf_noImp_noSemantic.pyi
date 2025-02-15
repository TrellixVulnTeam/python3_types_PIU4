from .prior import Prior
from torch.distributions import Gamma, MultivariateNormal, Normal
from typing import Any, Optional

MVN_LAZY_PROPERTIES: Any

class NormalPrior(Prior, Normal):
    _transform: Any = ...
    def __init__(self, loc: Any, scale: Any, validate_args: bool = ..., transform: Optional[Any] = ...) -> None: ...

class GammaPrior(Prior, Gamma):
    _transform: Any = ...
    def __init__(self, concentration: Any, rate: Any, validate_args: bool = ..., transform: Optional[Any] = ...) -> None: ...

class MultivariateNormalPrior(Prior, MultivariateNormal):
    _transform: Any = ...
    def __init__(self, loc: Any, covariance_matrix: Optional[Any] = ..., precision_matrix: Optional[Any] = ..., scale_tril: Optional[Any] = ..., validate_args: bool = ..., transform: Optional[Any] = ...) -> None: ...
    def cuda(self, device: Optional[Any] = ...): ...
    def cpu(self): ...
