from dataclasses import dataclass
from pywsp import MessageFactory, WebSocketMessage, message
from typing import Any, Dict, List

@message(type="event")
class EventMessage(WebSocketMessage):
    name: str
    args: Dict[str, Any]

@message(type="request_status")
class StatusRequestMessage(WebSocketMessage):
    args: List[str]

@dataclass
class Thermostat:
    serial_number: str
    last_updated: str
    status: Dict[str, Any]

@message(type="status_response")
class StatusResponseMessage(WebSocketMessage):
    last_updated: str
    thermostats: List[Thermostat]

message_factory = MessageFactory()
message_factory.register_message_types(
    EventMessage,
    StatusRequestMessage,
    StatusResponseMessage,
)
