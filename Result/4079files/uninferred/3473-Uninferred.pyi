from typing import Any
from unittest import TestCase

class ListOfSpeakersViewSetManageSpeaker(TestCase):
    request: Any = ...
    view_instance: Any = ...
    def setUp(self) -> None: ...
    def test_add_oneself_as_speaker(self, mock_speaker: Any, mock_has_perm: Any, mock_icd: Any) -> None: ...
    def test_add_someone_else_as_speaker(self, mock_speaker: Any, mock_get_user_model: Any, mock_has_perm: Any, mock_icd: Any) -> None: ...
    def test_remove_oneself(self, mock_speaker: Any) -> None: ...
    def test_remove_someone_else(self, mock_speaker: Any, mock_has_perm: Any, mock_inform_changed_data: Any) -> None: ...

class ListOfSpeakersViewSetSpeak(TestCase):
    request: Any = ...
    view_instance: Any = ...
    def setUp(self) -> None: ...
    def test_begin_speech(self) -> None: ...
    def test_begin_speech_specific_speaker(self, mock_speaker: Any) -> None: ...
    def test_end_speech(self, mock_speaker: Any) -> None: ...
