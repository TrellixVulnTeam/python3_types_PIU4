import pyshark.packet.packet
from typing import Any

class Flow:
    packets: Any = ...
    protocols: Any = ...
    logger: Any = ...
    start_time: Any = ...
    end_time: Any = ...
    client: Any = ...
    server: Any = ...
    def __init__(self, pkt: pyshark.packet.packet.Packet) -> None: ...
    def ingest(self, pkt: Any) -> None: ...
    def count_protocol(self, pkt: pyshark.packet.packet.Packet) -> Any: ...
    def __len__(self): ...
    def __str__(self): ...
    def __iter__(self) -> Any: ...

def check_if_packet_is_upstream(pkt: pyshark.packet.packet.Packet) -> Any: ...
