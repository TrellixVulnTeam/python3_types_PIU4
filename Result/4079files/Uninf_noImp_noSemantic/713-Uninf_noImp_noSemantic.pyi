from . import base
from typing import Any

class ProjectWikiSubView(base.SubView):
    project: Any = ...
    notifier: Any = ...
    wiki_page: Any = ...
    widget: Any = ...
    def __init__(self, parent_view: Any, project: Any, notifier: Any, tabs: Any) -> None: ...
