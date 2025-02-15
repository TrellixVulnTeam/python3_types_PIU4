from Crypto.PublicKey.RSA import RsaKey as RsaKey
from federation.entities.mixins import BaseEntity as BaseEntity
from federation.types import UserType
from lxml import etree
from typing import Any, Callable, List

logger: Any
MAPPINGS: Any
TAGS: Any
BOOLEAN_KEYS: Any
DATETIME_KEYS: Any
INTEGER_KEYS: Any

def xml_children_as_dict(node: Any): ...
def check_sender_and_entity_handle_match(sender_handle: Any, entity_handle: Any): ...
def element_to_objects(element: etree.ElementTree, sender: str, sender_key_fetcher: Callable[[str], str]=..., user: UserType=...) -> List: ...
def message_to_objects(message: str, sender: str, sender_key_fetcher: Callable[[str], str]=..., user: UserType=...) -> List: ...
def transform_attributes(attrs: Any, cls: Any): ...
def get_outbound_entity(entity: BaseEntity, private_key: RsaKey) -> Any: ...
