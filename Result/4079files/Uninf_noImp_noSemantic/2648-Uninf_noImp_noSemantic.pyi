import io
from vws import CloudRecoService, VWS

class TestQuery:
    def test_no_matches(self, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_match(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...

class TestCustomBaseVWQURL:
    def test_custom_base_url(self, high_quality_image: io.BytesIO) -> None: ...

class TestMaxNumResults:
    def test_default(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_custom(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_too_many(self, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...

class TestIncludeTargetData:
    def test_default(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_top(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_none(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
    def test_all(self, vws_client: VWS, cloud_reco_client: CloudRecoService, high_quality_image: io.BytesIO) -> None: ...
