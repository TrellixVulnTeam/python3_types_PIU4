from booking import Event as Event, EventsSource as EventsSource
from typing import Any, List

class GetTodayEventsUseCase:
    _events_source: Any = ...
    def __init__(self, events_source: EventsSource) -> None: ...
    def get_today_events(self, class_id: Any) -> List[Event]: ...
