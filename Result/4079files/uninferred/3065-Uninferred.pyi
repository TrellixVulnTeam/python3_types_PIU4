from tensorflow_model_analysis.eval_saved_model import testutil
from typing import Any

class UtilTest(testutil.TensorflowModelAnalysisTest):
    column_1: str = ...
    column_2: str = ...
    metrics_a: Any = ...
    slice_a: str = ...
    column_a: Any = ...
    result_a: Any = ...
    slice_b: str = ...
    metrics_b: Any = ...
    column_b: Any = ...
    result_b: Any = ...
    slice_c: str = ...
    metrics_c: Any = ...
    column_c: Any = ...
    result_c: Any = ...
    slice_d: str = ...
    metrics_d: Any = ...
    column_d: Any = ...
    result_d: Any = ...
    metrics_aggregate: Any = ...
    result_aggregate: Any = ...
    metrics_c2: Any = ...
    result_c2: Any = ...
    data_location_1: str = ...
    base_data_location_2: str = ...
    full_data_location_2: Any = ...
    model_location_1: str = ...
    base_model_location_2: str = ...
    full_model_location_2: Any = ...
    key: str = ...
    plots_data_a: Any = ...
    plots_a: Any = ...
    plots_data_b: Any = ...
    plots_b: Any = ...
    plots_data_b2: Any = ...
    plots_b2: Any = ...
    plots_data_c: Any = ...
    plots_c: Any = ...
    plots_data_c2: Any = ...
    plots_c2: Any = ...
    def _makeTestData(self): ...
    def _makeTestPlotsData(self): ...
    def _makeEvalResults(self): ...
    def _makeEvalConfig(self): ...
    def testGetSlicingMetrics(self) -> None: ...
    def testGetAggregateMetrics(self) -> None: ...
    def testFilterColumnResultBySpec(self) -> None: ...
    def testFilterFeatrueResultBySpec(self) -> None: ...
    def testFilterColumnCrossFeatrueResultBySpec(self) -> None: ...
    def testFilterFeatrueCrossResultBySpec(self) -> None: ...
    def testRaisesErrorWhenColumnNotAvailable(self) -> None: ...
    def testRaisesErrorWhenAggregateNotAvailable(self) -> None: ...
    def testRaisesErrorWhenMoreThanOneAggregateAvailable(self) -> None: ...
    def testFilterEvalResultsForTimeSeries(self) -> None: ...
    def testDisplayFullPathForTimeSeries(self) -> None: ...
    def testRaisesErrorWhenNoMatchAvailableInTimeSeries(self) -> None: ...
    def testRaisesErrorWhenToomManyMatchesAvailableInTimeSeries(self) -> None: ...
    def testGetPlotDataAndConfig(self) -> None: ...
    def testRaisesErrorWhenNoMatchAvailableInPlotData(self) -> None: ...
    def testRaisesErrorWhenMultipleSlicesMatchInPlotData(self) -> None: ...
    def testReplaceNaNInPlotWithNone(self) -> None: ...
    def testGetPlotUsingLabel(self) -> None: ...
    def testRaisesErrorWhenLabelNotProvided(self) -> None: ...
    def testRaisesErrorWhenNoMatchForLabel(self) -> None: ...
    def testRaisesErrorWhenMultipleMatchForLabel(self) -> None: ...
    def testGetSlicingConfig(self) -> None: ...
    def testOverrideWeightColumnForSlicingMetricsView(self) -> None: ...
