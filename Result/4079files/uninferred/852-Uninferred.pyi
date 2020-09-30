from typing import Any, Dict, List, Optional, Text, Tuple

def split_locale(locale: Text) -> Tuple[Text, Optional[Text]]: ...
def compare_locales(a: Any, b: Any): ...

class LocalesDict:
    dict: Any = ...
    _choice_cache: Any = ...
    def __init__(self) -> None: ...
    def list_locales(self) -> List[Optional[Text]]: ...
    def choose_locale(self, locale: Text) -> Text: ...

class LocalesFlatDict(LocalesDict):
    def update(self, new_data: Dict[Text, Dict[Text, Text]]) -> Any: ...