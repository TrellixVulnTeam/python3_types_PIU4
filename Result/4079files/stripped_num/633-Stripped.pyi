# (generated with --quick)

import collections
from typing import Any, Coroutine, Dict, Tuple, Type, TypeVar

IUPAC: Any
Seq: Any
SeqIO: Any
SeqRecord: Any
aiohttp: Any
asyncio: module
defaultdict: Type[collections.defaultdict]
ete3: Any
gzip: module
json: module
os: module
pd: Any
sys: module
tictax: Any
tqdm: Any
warnings: module

_T0 = TypeVar('_T0')
_T2 = TypeVar('_T2')

def annotate_diamond(records: _T0, diamond_path) -> _T0: ...
def build_record(id, classification) -> Any: ...
def classify_taxify(oc_session, ebi_session, sequence_id: _T2, sequence) -> Coroutine[Any, Any, Tuple[_T2, Dict[str, Any]]]: ...
def config() -> Any: ...
def filter_taxa(records, taxids, unclassified = ..., discard = ...) -> list: ...
def kmer_lca_records(seqs_path, one_codex_api_key = ..., fastq = ..., progress = ...) -> list: ...
def matrix(records, scafstats_path) -> Any: ...
def oc_classify(records, one_codex_api_key, progress = ..., stdout = ...) -> Coroutine[Any, Any, list]: ...
def oc_classify_single(session, sequence_id, sequence) -> Coroutine[Any, Any, Dict[str, Any]]: ...
def parse_seqs(seqs_path, fastq = ...) -> list: ...
def taxify_ebi(session, sequence_id, taxid) -> Coroutine[Any, Any, Dict[str, Any]]: ...