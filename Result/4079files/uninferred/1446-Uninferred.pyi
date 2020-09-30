import apache_beam as beam
from tensorflow_data_validation import types as types
from tensorflow_data_validation.statistics import stats_options
from typing import Any, Generator

class GenerateStatistics(beam.PTransform):
    _options: Any = ...
    def __init__(self, options: stats_options.StatsOptions=...) -> None: ...
    def expand(self, dataset: beam.pvalue.PCollection) -> beam.pvalue.PCollection: ...

def _sample_at_rate(example: types.Example, sample_rate: float) -> Generator[types.Example, None, None]: ...