from haystack.generic_views import SearchView
from typing import Any

class ProjectSearchView(SearchView):
    template_name: str = ...
    form_class: Any = ...
    paginate_by: int = ...
    queryset: Any = ...
    def get_context_data(self, **kwargs: Any): ...

def autocomplete(request: Any): ...
