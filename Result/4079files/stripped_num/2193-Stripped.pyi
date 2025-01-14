# (generated with --quick)

from typing import Any, Optional, Tuple

FancyArrowPatch: Any
VonMisesFisherMixture: Any
mplstereonet: Any
np: module
plt: Any
proj3d: Any

class vMF:
    kappa: Any
    mean: Any
    name: Any
    num_samples: Any
    samples_azdip: Any
    samples_xyz: Any
    def __init__(self, name = ..., mean = ..., kappa = ...) -> None: ...
    def __repr__(self) -> str: ...
    def _cartesian2spherical(self, xyz) -> Any: ...
    def _generate_samples(self) -> Any: ...
    def _sample_orthonormal_to(self) -> Any: ...
    def _sample_weight(self, dim) -> Any: ...
    def _spherical2cartesian(self, orient) -> Any: ...
    def add_orientation_data(self, orient) -> None: ...
    def cart2sph_real(self, xyz) -> Any: ...
    def estimate_vMF_params(self) -> None: ...
    def plot_samples_3D(self) -> Any: ...
    def plot_stereonet(self, poles = ..., samples = ...) -> None: ...
    def sample(self, mean = ..., kappa = ..., num_samples = ..., direct_output = ...) -> Optional[Tuple[Any, Any]]: ...
