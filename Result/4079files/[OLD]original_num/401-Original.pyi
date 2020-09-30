# (generated with --quick)

from typing import Any, Optional, Union

HEADERS: Any
json: module
requests: module

def create_cfg_segment(filename, filecontent, description, auth, url) -> Optional[Union[int, str]]: ...
def delete_cfg_template(template_name, auth, url) -> Optional[Union[int, str]]: ...
def get_cfg_template(auth, url, folder = ...) -> Any: ...
def get_folder_id(folder_name, auth, url) -> Union[int, str]: ...
def get_template_details(template_name, auth, url) -> Any: ...
def get_template_id(template_name, auth, url) -> Union[int, str]: ...