from lxml import objectify
from memsource import models
from typing import Any

class MxliffParser:
    score_key: Any = ...
    gloss_score_key: Any = ...
    tunit_metadata_key: Any = ...
    mark_key: Any = ...
    type_key: Any = ...
    content_key: Any = ...
    def parse(self, resource: None) -> Any: ...
    def parse_group(self, group: objectify.ObjectifiedElement) -> models.MxliffUnit: ...
    def parse_tunit_metadata(self, trans_unit: objectify.ObjectifiedElement) -> list: ...
