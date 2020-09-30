from gitlabform.gitlab.core import GitLabCore
from typing import Any, Optional

class GitLabMergeRequests(GitLabCore):
    def create_mr(self, project_and_group_name: Any, source_branch: Any, target_branch: Any, title: Any, description: Optional[Any] = ...): ...
    def accept_mr(self, project_and_group_name: Any, mr_iid: Any): ...
    def update_mr(self, project_and_group_name: Any, mr_iid: Any, data: Any) -> None: ...
    def get_mrs(self, project_and_group_name: Any): ...
    def get_mr(self, project_and_group_name: Any, mr_iid: Any): ...
    def get_mr_approvals(self, project_and_group_name: Any, mr_iid: Any): ...