import numpy as np
from .image import SingleConditionSpec
from nibabel.spatialimages import SpatialImage
from pathlib import Path
from typing import Callable, Iterable, List, Union

def load_images_from_dir(in_dir: Union[str, Path], suffix: str=...) -> Iterable[SpatialImage]: ...
def load_images(image_paths: Iterable[Union[str, Path]]) -> Iterable[SpatialImage]: ...
def load_boolean_mask(path: Union[str, Path], predicate: Callable[[np.ndarray], np.ndarray]=...) -> np.ndarray: ...
def load_labels(path: Union[str, Path]) -> List[SingleConditionSpec]: ...
def save_as_nifti_file(data: np.ndarray, affine: np.ndarray, path: Union[str, Path]) -> None: ...
