from typing import Any

client: Any
loop: Any
re_chan: Any
re_link: Any
re_user: Any

def send_user_dm(u_id: Any, text: Any): ...
def get_all_channels(): ...
def get_all_users(): ...
def get_user_name_by_id(user_id: Any): ...
def get_user_message_history(user_name: Any, channels: Any): ...
def sanitize_chan_str(txt: Any, match: Any): ...
def sanitize_link_str(txt: Any, match: Any): ...
def sanitize_user_str(txt: Any, match: Any): ...
def sanitize_slack_str(text: Any): ...
