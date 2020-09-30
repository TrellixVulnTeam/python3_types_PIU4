import gpytorch
import unittest
from torch import nn
from typing import Any

def make_data(cuda: bool = ...): ...

data_dim: int

class SmallFeatureExtractor(nn.Sequential):
    def __init__(self) -> None: ...

feature_extractor: Any

class GPRegressionModel(gpytorch.models.ExactGP):
    mean_module: Any = ...
    base_covar_module: Any = ...
    covar_module: Any = ...
    feature_extractor: Any = ...
    def __init__(self, train_x: Any, train_y: Any, likelihood: Any) -> None: ...
    def forward(self, x: Any): ...

class TestDKLRegression(unittest.TestCase):
    rng_state: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_dkl_gp_mean_abs_error(self) -> None: ...
    def test_dkl_gp_fast_pred_var(self) -> None: ...