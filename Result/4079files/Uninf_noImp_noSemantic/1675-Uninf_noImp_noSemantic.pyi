import unittest
from typing import Any

class ReorientJobbingImporterTestCase(unittest.TestCase):
    data_folder: Any = ...
    market_score: Any = ...
    offers_csv: Any = ...
    rome_job_groups: Any = ...
    item_arborescence: Any = ...
    referentiel_apellation: Any = ...
    def test_csv2dicts(self) -> None: ...
