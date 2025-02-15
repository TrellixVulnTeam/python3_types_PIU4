import datetime
import pandas as pd
import netanalysis.traffic.data.model as traffic
from netanalysis.traffic.analysis import model
from typing import Any, Iterable, List

def get_expectations_1(time_series: pd.Series) -> pd.DataFrame: ...
def find_anomalies(time_series: pd.Series) -> List[model.AnomalyPoint]: ...
def group_as_product_disruptions(product_id: traffic.ProductId, anomalies: Iterable[model.AnomalyPoint], max_time_delta: datetime.timedelta) -> List[model.ProductDisruption]: ...
def remove_minor_disruptions(product_disruptions: List[model.ProductDisruption]) -> List[model.ProductDisruption]: ...
def group_as_regional_disruptions(region_code: str, product_disruptions: List[model.ProductDisruption]) -> List[model.RegionDisruption]: ...
def _to_google_timestamp(timestamp: datetime.datetime) -> Any: ...
def _make_report_url(start_date: datetime.datetime, end_date: datetime.datetime, region_code: str, product_id: traffic.ProductId) -> Any: ...
def _make_tor_users_url(start_date: datetime.datetime, end_date: datetime.datetime, region_code: str) -> Any: ...
def _make_context_web_search_url(start_date: datetime.datetime, end_date: datetime.datetime, region_code: str) -> Any: ...
def _make_context_twitter_url(start_date: datetime.datetime, end_date: datetime.datetime, region_code: str) -> Any: ...
def print_disruption_csv(disruption: model.RegionDisruption) -> None: ...
def find_all_disruptions(repo: traffic.TrafficRepository, regions: Iterable[str], products: Iterable[traffic.ProductId]) -> List[model.RegionDisruption]: ...
def main(args: Any): ...
