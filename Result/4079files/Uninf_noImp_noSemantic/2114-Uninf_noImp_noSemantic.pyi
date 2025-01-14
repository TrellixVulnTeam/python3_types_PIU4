import unittest
from typing import Any, Optional

def enable_logging(level: Any = ..., handler: Optional[Any] = ..., formatter: Optional[Any] = ...) -> None: ...

class TestCommonUtils(unittest.TestCase):
    def test_uuid(self) -> None: ...
    def test_uuid_generate(self) -> None: ...
    def test_uuid_validate(self) -> None: ...
    def test_bytes_to_utf8_0(self) -> None: ...
    def test_bytes_to_utf8_1(self) -> None: ...
    def test_bytes_to_utf8_2(self) -> None: ...
    def test_bytes_to_utf8_3(self) -> None: ...
    def test_save_to_file0(self, m_open: Any): ...
    def test_save_to_file1(self, m_open: Any): ...
    def test_irma_taskreturn_success(self) -> None: ...
    def test_irma_taskreturn_warning(self) -> None: ...
    def test_irma_taskreturn_error(self) -> None: ...
    def test_irma_frontendreturn_success(self) -> None: ...
    def test_irma_frontendreturn_warning(self) -> None: ...
    def test_irma_frontendreturn_error(self) -> None: ...
    def test_irmascanstatus_is_error0(self) -> None: ...
    def test_irmascanstatus_is_error1(self) -> None: ...
    def test_irmascanstatus_is_error2(self) -> None: ...
    def test_irmascanstatus_filter_status0(self) -> None: ...
    def test_irmascanstatus_filter_status1(self) -> None: ...
    def test_irmascanstatus_filter_status2(self) -> None: ...
    def test_irmascanstatus_filter_status3(self) -> None: ...
    def test_irmascanstatus_code_ot_label0(self) -> None: ...
    def test_irmascanstatus_code_ot_label1(self) -> None: ...
    def test_irmaprobetype_normalize0(self) -> None: ...
    def test_irmaprobetype_normalize1(self) -> None: ...
    def test_common_celery_options0(self, m_generate: Any) -> None: ...
    def test_common_celery_options1(self, m_generate: Any) -> None: ...

class TestIrmaScanRequest(unittest.TestCase):
    isr: Any = ...
    def setUp(self) -> None: ...
    def test_init(self) -> None: ...
    def test_add_file(self) -> None: ...
    def test_del_file0(self) -> None: ...
    def test_del_file1(self) -> None: ...
    def test_get_probelist(self) -> None: ...
    def test_set_probelist(self) -> None: ...
    def test_get_mimetype(self) -> None: ...
    def test_to_dict(self) -> None: ...
    def test_files(self) -> None: ...
