# (generated with --quick)

from typing import Any, Generator, Optional

base64: module
i: Any
j: JIRA
json: module
requests: module
sys: module

class GitHub(object):
    org: Any
    password: Any
    url: str
    user: Any
    def __init__(self, user, password, org = ...) -> None: ...
    def closeIssue(self, issue_json) -> Any: ...
    def commentOnIssue(self, issue_json, comment) -> Any: ...
    def getAuth(self) -> str: ...
    def getOrgRepositories(self) -> Optional[list]: ...
    def getShortRepositories(self) -> Optional[list]: ...

class GitHubRepository(GitHub):
    org: Any
    password: Any
    repo: Any
    url: str
    user: Any
    def __init__(self, repo, user, password, org) -> None: ...
    def getAllIssues(self) -> Any: ...
    def getAllPullRequests(self) -> Any: ...

class JIRA(object):
    password: Any
    url: Any
    user: Any
    def __init__(self, url, user, password) -> None: ...
    def closeDuplicateIssue(self, orig_issue, dup_issue) -> bool: ...
    def closeIssue(self, issue, comment = ..., resolution = ...) -> bool: ...
    def commentOnIssue(self, issue, comment) -> bool: ...
    def createIssue(self, project, title, description, issuetype = ..., extrafields = ...) -> Any: ...
    def createSubTask(self, parentkey, project, title, description) -> Any: ...
    def getAllIssues(self, params = ...) -> Any: ...
    def getAuth(self) -> str: ...
    def issues_iter(self, jql) -> Generator[Any, Any, None]: ...

def gen_base64(username, password) -> str: ...
