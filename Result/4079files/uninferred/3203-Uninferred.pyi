from channels.tests import ChannelTestCase

class TestDatasetBinding(ChannelTestCase):
    def test_outbound_create(self) -> None: ...

class TestCalculationBinding(ChannelTestCase):
    def test_outbound_create(self) -> None: ...
    def test_outbound_create_fixed_feature_set(self) -> None: ...
