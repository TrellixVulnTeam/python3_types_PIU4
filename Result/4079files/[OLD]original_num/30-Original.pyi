# (generated with --quick)

from typing import Any

ApplicationFactory: Any
GroupFactory: Any
GroupNotificationType: Any
PickupDateFactory: Any
PlaceFactory: Any
TestCase: Any
UserFactory: Any
generate_token: Any
parse_token: Any
unsubscribe_from_all_conversations_in_group: Any
unsubscribe_from_notification_type: Any

class TestTokenParser(Any):
    group: Any
    user: Any
    def setUp(self) -> None: ...
    def test_with_a_conversation(self) -> None: ...
    def test_with_a_thread(self) -> None: ...
    def test_with_notification_types(self) -> None: ...

class TestUnsubscribeFromAllConversationsInGroup(Any):
    group: Any
    other_group: Any
    other_place: Any
    place: Any
    user: Any
    def setUp(self) -> None: ...
    def test_does_not_unsubscribe_from_other_group_pickup_conversations(self) -> None: ...
    def test_does_not_unsubscribe_from_other_group_wall(self) -> None: ...
    def test_unsubscribe_from_all_group_notifications(self) -> None: ...
    def test_unsubscribe_from_applications(self) -> None: ...
    def test_unsubscribe_from_group_wall(self) -> None: ...
    def test_unsubscribe_from_group_wall_thread(self) -> None: ...
    def test_unsubscribe_from_pickup_conversation(self) -> None: ...

class TestUnsubscribeFromNotificationTypes(Any):
    group: Any
    user: Any
    def setUp(self) -> None: ...
    def test_unsubscribe_from_weekly_summaries(self) -> None: ...