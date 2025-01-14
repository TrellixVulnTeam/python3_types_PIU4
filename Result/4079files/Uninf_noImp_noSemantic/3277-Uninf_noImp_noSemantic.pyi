from typing import Any

class WorkflowyScheduler:
    workflowy_url: str = ...
    browser: Any = ...
    @classmethod
    def schedule_items_for_today(cls) -> None: ...
    @classmethod
    def __login(cls) -> None: ...
    @classmethod
    def __search(cls: Any, search_term: str) -> Any: ...
    @classmethod
    def __mark_results_with_tag(cls: Any, tag: str) -> Any: ...
    @classmethod
    def __save_changes(cls) -> None: ...
    @classmethod
    def __click_button(cls: Any, css_selector: str) -> Any: ...
    @classmethod
    def __wait_for_element_to_appear(cls, css_selector: Any): ...
    @classmethod
    def __fill_text_box(cls: Any, css_selector: str, text_to_input: str) -> Any: ...
    @classmethod
    def __get_todays_date_tag(cls: Any) -> str: ...
