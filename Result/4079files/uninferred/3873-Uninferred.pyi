from PIL import ImageColor as ImageColor
from typing import Any

class MeasureVisualizer:
    draw_system_measures: Any = ...
    draw_stave_measures: Any = ...
    draw_staves: Any = ...
    def __init__(self, draw_system_measures: bool, draw_stave_measures: bool, draw_staves: bool) -> None: ...
    def draw_bounding_boxes_for_all_images_in_directory(self, image_directory: Any, json_annotation_directory: Any) -> None: ...
    def draw_bounding_boxes_into_image(self, image_path: str, ground_truth_annotations_path: str) -> Any: ...
    def _draw_rectangles(self, rectangles: Any, image: Any, color: Any) -> None: ...
