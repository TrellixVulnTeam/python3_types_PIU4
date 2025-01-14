# (generated with --quick)

import gramtool.grammar
import gramtool.hunspell
from typing import Any, Dict, Type

Grammar: Type[gramtool.grammar.Grammar]
_dicts: Dict[Any, Wrapper]
os: module
pres: module

class Wrapper(object):
    grammar: gramtool.grammar.Grammar
    hunspell: gramtool.hunspell.HunSpell
    rules: Any
    tree: Any
    def __init__(self, lang) -> None: ...

def _get_lemma(word, lang) -> Any: ...
def _get_stem(word, lang) -> Any: ...
def get_grammar_rules(tree, filename) -> Any: ...
def get_grammar_tree(filename) -> Any: ...
def get_hunspell_dict(aff, dic) -> gramtool.hunspell.HunSpell: ...
def lemma(word, lang = ...) -> Any: ...
def load(lang) -> Wrapper: ...
