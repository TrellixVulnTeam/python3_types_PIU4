from typing import Any
from xml.etree.ElementTree import ElementTree

config: Any

def parseHml(fileName: str) -> ElementTree: ...
def convertEquation(doc: ElementTree) -> str: ...
def extract2HtmlStr(doc: ElementTree) -> str: ...
