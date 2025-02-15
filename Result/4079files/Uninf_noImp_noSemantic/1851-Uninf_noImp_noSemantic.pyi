from errbot import BotPlugin
from typing import Any
from utils.mixin import DefaultConfigMixin

class Answer(DefaultConfigMixin, BotPlugin):
    CONFIG_TEMPLATE: Any = ...
    SURVEY_LINK: str = ...
    MESSAGE_LINK: str = ...
    @staticmethod
    def construct_link(text: Any): ...
    def answer(self, msg: Any, arg: Any): ...
