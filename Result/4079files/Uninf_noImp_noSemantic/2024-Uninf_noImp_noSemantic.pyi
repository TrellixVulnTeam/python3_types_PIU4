from src.page_object_pattern.base_page import BasePage

class SearchPage(BasePage):
    HEADING: str = ...
    SEE_ALSO: str = ...
    DOMAIN_ARTICLES: str = ...
    READING: str = ...
    REF: str = ...
    EXTERNAL_LINKS: str = ...
    def heading_text(self): ...
    def see_also_text(self): ...
    def domain_articles_text(self): ...
    def reading_text(self): ...
    def ref_text(self): ...
    def external_links_text(self): ...