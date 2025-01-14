# (generated with --quick)

from typing import Any
import unittest.case

Container: Any
Deck: Any
Slot: Any
Vector: Any
Well: Any
math: module
unittest: module

class PlaceableTestCase(unittest.case.TestCase):
    def assertWellSeriesEqual(self, w1, w2) -> None: ...
    def generate_plate(self, wells, cols, spacing, offset, radius, height = ...) -> Any: ...
    def test_add_placeables(self) -> None: ...
    def test_chain_method(self) -> None: ...
    def test_coordinates(self) -> None: ...
    def test_cycle(self) -> None: ...
    def test_generate_plate(self) -> None: ...
    def test_get_all_children(self) -> None: ...
    def test_get_container_name(self) -> None: ...
    def test_get_name(self) -> None: ...
    def test_int_index(self) -> None: ...
    def test_iter_method(self) -> None: ...
    def test_iterator(self) -> None: ...
    def test_max_dimensions(self) -> None: ...
    def test_named_well(self) -> None: ...
    def test_next(self) -> None: ...
    def test_slice_with_strings(self) -> None: ...
    def test_top_bottom(self) -> None: ...
    def test_well_from_center(self) -> None: ...
    def test_wells(self) -> None: ...
