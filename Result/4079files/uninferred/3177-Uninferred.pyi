from typing import Any

class Tables:
    def get_sentence_table(self, tablename: str = ...): ...
    def get_wordprobability_table(self, tablename: Any): ...
    def get_wordalignment_table(self, tablename: Any): ...
    def get_phrase_table(self, tablename: str = ...): ...
    def get_transphraseprob_table(self, tablename: str = ...): ...
    def get_trigram_table(self, tablename: Any): ...
    def get_trigramprob_table(self, tablename: Any): ...
    def get_trigramprobwithoutlast_table(self, tablename: Any): ...
    def get_unigram_table(self, tablename: Any): ...
    def get_unigramprob_table(self, tablename: Any): ...
