# (generated with --quick)

import numpy
from typing import Any, List, Optional, Tuple

INPUT_IMAGE_DIR: str
INTERPOLATED_IMAGE_DIR: str
TRUE_IMAGE_DIR: str
configparser: module
logging: module
misc: Any
np: module
os: module
random: module
util: Any

class BatchDataSets:
    batch_dir: Any
    batch_image_size: Any
    batch_index: Optional[List[int]]
    channels: Any
    count: int
    index: int
    input_images: Optional[numpy.ndarray]
    input_interpolated_images: Optional[numpy.ndarray]
    resampling_method: Any
    scale: Any
    stride: Any
    true_images: Optional[numpy.ndarray]
    def __init__(self, scale, batch_dir, batch_image_size, stride_size = ..., channels = ..., resampling_method = ...) -> None: ...
    def build_batch(self, data_dir) -> None: ...
    def get_next_image_no(self) -> Any: ...
    def init_batch_index(self) -> None: ...
    def is_batch_exist(self) -> bool: ...
    def load_all_batch_images(self) -> None: ...
    def load_batch_counts(self) -> None: ...
    def load_batch_image(self, max_value) -> Tuple[Any, Any, Any]: ...
    def load_batch_image_from_disk(self, image_number) -> Tuple[Any, Any, Any]: ...
    def load_input_batch_image(self, image_number) -> Any: ...
    def load_interpolated_batch_image(self, image_number) -> Any: ...
    def load_true_batch_image(self, image_number) -> Any: ...
    def release_batch_images(self) -> None: ...
    def save_input_batch_image(self, image_number, image) -> Any: ...
    def save_interpolated_batch_image(self, image_number, image) -> Any: ...
    def save_true_batch_image(self, image_number, image) -> Any: ...

class DynamicDataSets:
    batch_image_size: Any
    batch_index: Optional[List[int]]
    channels: Any
    count: int
    filenames: Any
    index: int
    resampling_method: Any
    scale: Any
    def __init__(self, scale, batch_image_size, channels = ..., resampling_method = ...) -> None: ...
    def get_next_image_no(self) -> Any: ...
    def init_batch_index(self) -> None: ...
    def load_batch_image(self, max_value) -> Any: ...
    def load_random_patch(self, filename) -> Any: ...
    def set_data_dir(self, data_dir) -> None: ...

def build_image_set(file_path, channels = ..., scale = ..., convert_ycbcr = ..., resampling_method = ..., print_console = ...) -> Tuple[Any, Any, Any]: ...
def build_input_image(image, width = ..., height = ..., channels = ..., scale = ..., alignment = ..., convert_ycbcr = ...) -> Any: ...
def load_input_image(filename, width = ..., height = ..., channels = ..., scale = ..., alignment = ..., convert_ycbcr = ..., print_console = ...) -> Any: ...
