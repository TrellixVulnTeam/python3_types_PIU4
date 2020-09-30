import unittest
from pycqed.instrument_drivers.meta_instrument.qubit_objects.CC_transmon import CBox_v3_driven_transmon as CBox_v3_driven_transmon, QWG_driven_transmon as QWG_driven_transmon
from pycqed.instrument_drivers.meta_instrument.qubit_objects.QuDev_transmon import QuDev_transmon as QuDev_transmon
from pycqed.instrument_drivers.meta_instrument.qubit_objects.Tektronix_driven_transmon import Tektronix_driven_transmon as Tektronix_driven_transmon
from pycqed.instrument_drivers.physical_instruments.QuTech_CCL import CCL as CCL
from pycqed.instrument_drivers.physical_instruments.QuTech_QCC import QCC as QCC
from typing import Any

openql_import_fail: bool

class Test_Device_obj(unittest.TestCase):
    station: Any = ...
    CCL_qubit: Any = ...
    MW1: Any = ...
    MW2: Any = ...
    MW3: Any = ...
    SH: Any = ...
    UHFQC: Any = ...
    CCL: Any = ...
    QCC: Any = ...
    VSM: Any = ...
    MC: Any = ...
    AWG_mw_0: Any = ...
    AWG_mw_1: Any = ...
    AWG_flux_0: Any = ...
    AWG8_VSM_MW_LutMan: Any = ...
    ro_lutman: Any = ...
    device: Any = ...
    @classmethod
    def setUpClass(self) -> None: ...
    def test_get_dio_map(self) -> None: ...
    def test_prepare_timing_CCL(self) -> None: ...
    def test_prepare_timing_QCC(self) -> None: ...
    def test_prepare_timing_QCC_fine(self) -> None: ...
    @classmethod
    def tearDownClass(self) -> None: ...