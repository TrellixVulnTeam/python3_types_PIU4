from typing import Any

user_id: Any
api_key: Any
qb_host: Any
QB_QUESTION_DB: str
base_url: Any
server: Any

class ThresholdBuzzer:
    threshold: Any = ...
    def __init__(self, threshold: float = ...) -> None: ...
    def normalize(self, scores: Any): ...
    def buzz(self, guesses: Any, position: Any): ...

def submit_answer(qid: Any, answer: Any) -> None: ...
def get_word(qid: Any, i: Any): ...
def main(): ...
