from typing import Any

def get_spectrum_y_bound(pix: Any, x: Any, middle_y: Any, spectrum_threshold: Any, spectrum_threshold_duration: Any): ...
def find_aperture(pic_pixels: Any, pic_width: int, pic_height: int) -> object: ...
def draw_aperture(aperture: Any, draw: Any) -> None: ...
def draw_scan_line(aperture: Any, draw: Any, spectrum_angle: Any) -> None: ...
def wavelength_to_color(lambda2: Any): ...
def take_picture(name: Any, shutter: Any): ...
def draw_graph(draw: Any, pic_pixels: Any, aperture: object, spectrum_angle: Any, wavelength_factor: Any) -> Any: ...
def draw_ticks_and_frequencies(draw: Any, aperture: Any, spectrum_angle: Any, wavelength_factor: Any) -> None: ...
def inform_user_of_exposure(max_result: Any) -> None: ...
def save_image_with_overlay(im: Any, name: Any) -> None: ...
def normalize_results(results: Any, max_result: Any): ...
def export_csv(name: Any, normalized_results: Any) -> None: ...
def export_diagram(name: Any, normalized_results: Any) -> None: ...
def main() -> None: ...