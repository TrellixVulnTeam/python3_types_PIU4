# (generated with --quick)

import collections
from typing import Any, Callable, Tuple, Type, TypeVar

OrderedDict: Type[collections.OrderedDict]
datetime: Type[datetime.datetime]

_T2 = TypeVar('_T2')

def active_memberships(project) -> collections.OrderedDict: ...
def assigned_points(project_stats) -> Any: ...
def closed_issues(issues_stats) -> Any: ...
def closed_points(project_stats) -> Any: ...
def color(user, default_color = ...) -> Any: ...
def completed_milestones(project) -> list: ...
def computable_roles(project) -> collections.OrderedDict: ...
def content(wiki_page) -> Any: ...
def current_milestone(project) -> Any: ...
def current_milestone_name(project) -> Any: ...
def date(text, date_format = ...) -> datetime.datetime: ...
def defined_points(project_stats) -> Any: ...
def defined_points_percentage(project_stats) -> Any: ...
def doomline_limit_points(project_stats) -> Any: ...
def issue_assigned_to_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_owner_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_priority_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_ref(issue) -> Any: ...
def issue_severity_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_status_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_statuses(project) -> collections.OrderedDict[str, Any]: ...
def issue_subject(issue) -> Any: ...
def issue_type_with_color(issue, project, default_color: _T2 = ...) -> Tuple[Any, Any]: ...
def issue_types(project) -> collections.OrderedDict[str, Any]: ...
def issues_priorities_stats(issues_stats) -> Any: ...
def issues_severities_stats(issues_stats) -> Any: ...
def issues_statuses_stats(issues_stats) -> Any: ...
def itemgetter(*items) -> Callable[[Any], tuple]: ...
def list_of_milestones(project, reverse = ...) -> list: ...
def milestone_closed_points(milestone) -> Any: ...
def milestone_completed_points(milestone_stats) -> Any: ...
def milestone_completed_tasks(milestone_stats) -> Any: ...
def milestone_estimated_finish(milestone_stats) -> Any: ...
def milestone_estimated_start(milestone_stats) -> Any: ...
def milestone_finish_date(milestone) -> Any: ...
def milestone_name(milestone) -> Any: ...
def milestone_remaining_days(milestone_stats) -> int: ...
def milestone_total_points(milestone_stats) -> Any: ...
def milestone_total_tasks(milestone_stats) -> Any: ...
def milestones_are_equals(milestone1, milestone2) -> Any: ...
def opened_issues(issues_stats) -> Any: ...
def points(project) -> collections.OrderedDict[str, Any]: ...
def priorities(project) -> collections.OrderedDict[str, Any]: ...
def severities(project) -> collections.OrderedDict[str, Any]: ...
def slug(wiki_page) -> Any: ...
def task_finished_date(task) -> Any: ...
def task_ref(task) -> Any: ...
def task_statuses(project) -> collections.OrderedDict[str, Any]: ...
def task_subject(task) -> Any: ...
def tasks_per_user_story(tasks, user_story) -> list: ...
def total_issues(issues_stats) -> Any: ...
def total_milestones(project_stats) -> Any: ...
def total_points(project_stats) -> Any: ...
def unassigned_tasks(tasks) -> list: ...
def us_client_requirement(us) -> Any: ...
def us_is_blocked(us) -> Any: ...
def us_ref(us) -> Any: ...
def us_statuses(project) -> collections.OrderedDict[str, Any]: ...
def us_subject(us) -> Any: ...
def us_team_requirement(us) -> Any: ...
def us_total_points(us) -> Any: ...
def user_full_name(user) -> Any: ...