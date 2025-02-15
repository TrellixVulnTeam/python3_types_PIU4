from typing import Any, Optional

def gen_base64(username: Any, password: Any): ...

class JIRA:
    url: Any = ...
    user: Any = ...
    password: Any = ...
    def __init__(self, url: Any, user: Any, password: Any) -> None: ...
    def getAuth(self): ...
    def getAllIssues(self, params: Any = ...): ...
    def issues_iter(self, jql: Any) -> None: ...
    def createIssue(self, project: Any, title: Any, description: Any, issuetype: str = ..., extrafields: Any = ...): ...
    def createSubTask(self, parentkey: Any, project: Any, title: Any, description: Any): ...
    def closeIssue(self, issue: Any, comment: Optional[Any] = ..., resolution: str = ...): ...
    def commentOnIssue(self, issue: Any, comment: Any): ...
    def closeDuplicateIssue(self, orig_issue: Any, dup_issue: Any): ...

class GitHub:
    url: str = ...
    user: Any = ...
    password: Any = ...
    org: Any = ...
    def __init__(self, user: Any, password: Any, org: Optional[Any] = ...) -> None: ...
    def getAuth(self): ...
    def getOrgRepositories(self): ...
    def getShortRepositories(self): ...
    def commentOnIssue(self, issue_json: Any, comment: Any): ...
    def closeIssue(self, issue_json: Any): ...

class GitHubRepository(GitHub):
    repo: Any = ...
    def __init__(self, repo: Any, user: Any, password: Any, org: Any) -> None: ...
    def getAllPullRequests(self): ...
    def getAllIssues(self): ...
