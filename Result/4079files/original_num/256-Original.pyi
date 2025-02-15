# (generated with --quick)

from typing import Any, Callable, IO, Iterable, Mapping, Tuple
import xml.etree.ElementTree

Asset: Any
ET: module
MetadataProcessor: Any
Processor: Any
UnsupportedFormatError: Any
XML_NS: dict
_FONT_SIZE_PT: int
_INCH_TO_MM: float
_PT_PER_INCH: float
_PX_PER_INCH: int
_X_HEIGHT: float
io: module
operator: Any

class SVGMetadataProcessor(Any):
    __doc__: str
    formats: Iterable[str]
    def __init__(self) -> None: ...
    def combine(self, file: IO, metadata: Mapping[str, Mapping]) -> IO: ...
    def read(self, file: IO) -> Mapping[str, Mapping]: ...
    def strip(self, file: IO) -> IO: ...

class SVGProcessor(Any):
    __doc__: str
    shrink: Any
    @staticmethod
    def _SVGProcessor__remove_elements(root: xml.etree.ElementTree.Element, qname: str, keep_func: Callable[[xml.etree.ElementTree.Element], bool]) -> None: ...
    @staticmethod
    def _SVGProcessor__remove_xml_whitespace(elem: xml.etree.ElementTree.Element) -> None: ...
    def __init__(self) -> None: ...
    def can_read(self, file: IO) -> bool: ...
    def read(self, file: IO) -> Any: ...

def _parse_svg(file: IO) -> Tuple[xml.etree.ElementTree.ElementTree, xml.etree.ElementTree.Element]: ...
def _register_xml_namespaces() -> None: ...
def _write_svg(tree: xml.etree.ElementTree.ElementTree) -> IO: ...
def svg_length_to_px(length: str) -> float: ...
