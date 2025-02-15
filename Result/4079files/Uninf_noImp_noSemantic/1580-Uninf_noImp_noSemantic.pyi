from SNOMEDCTToOWL.SNOMEDToOWLConstants import *
from .RF2File import RF2File
from .Transitive import Transitive
from SNOMEDCTToOWL.TransformationContext import TransformationContext
from typing import Any, Dict, List

LanguageName = str

class Language:
    lang: Any = ...
    acceptabilityId: Any = ...
    def __init__(self, row: Dict, context: TransformationContext) -> None: ...

class Languages(RF2File):
    prefix: Any = ...
    _members: Any = ...
    def __init__(self) -> None: ...
    def add(self, row: Dict, context: TransformationContext, _: Transitive) -> None: ...
    def preferred(self, descid: SCTID) -> List[LanguageName]: ...
    def acceptable(self, descid: SCTID) -> List[LanguageName]: ...
    def _filter_langs(self, entryid: SCTID, acceptability: SCTID) -> List[LanguageName]: ...
