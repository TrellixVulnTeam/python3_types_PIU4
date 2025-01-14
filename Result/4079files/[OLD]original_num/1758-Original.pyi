# (generated with --quick)

from typing import Any
import unittest.case

core: Any
static: Any
structs: Any
translate: Any
unittest: module

class TestMetar(unittest.case.TestCase):
    def test_cardinal_direction(self) -> None: ...
    def test_metar(self) -> None: ...
    def test_temperature(self) -> None: ...
    def test_wind(self) -> None: ...

class TestShared(unittest.case.TestCase):
    def test_altimeter(self) -> None: ...
    def test_clouds(self) -> None: ...
    def test_other_list(self) -> None: ...
    def test_shared(self) -> None: ...
    def test_visibility(self) -> None: ...
    def test_wxcode(self) -> None: ...

class TestTaf(unittest.case.TestCase):
    def test_min_max_temp(self) -> None: ...
    def test_taf(self) -> None: ...
    def test_turb_ice(self) -> None: ...
    def test_wind_shear(self) -> None: ...
