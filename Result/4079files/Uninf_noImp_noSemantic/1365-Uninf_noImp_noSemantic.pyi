from ..core.championmastery import ChampionMasteries, ChampionMastery, ChampionMasteryData, ChampionMasteryListData
from ..dto.championmastery import ChampionMasteryDto, ChampionMasteryListDto
from datapipelines import DataTransformer, PipelineContext
from typing import Type, TypeVar

T = TypeVar('T')
F = TypeVar('F')

class ChampionMasteryTransformer(DataTransformer):
    def transform(self, target_type: Type[T], value: F, context: PipelineContext=...) -> T: ...
    def champion_mastery_dto_to_data(self, value: ChampionMasteryDto, context: PipelineContext=...) -> ChampionMasteryData: ...
    def champion_mastery_list_dto_to_data(self, value: ChampionMasteryListDto, context: PipelineContext=...) -> ChampionMasteryListData: ...
    def champion_mastery_data_to_core(self, value: ChampionMasteryData, context: PipelineContext=...) -> ChampionMastery: ...
    def champion_mastery_list_data_to_core(self, value: ChampionMasteryListData, context: PipelineContext=...) -> ChampionMasteries: ...
