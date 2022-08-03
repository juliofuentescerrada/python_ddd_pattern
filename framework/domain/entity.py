import abc
from typing import TypeVar, Generic, List, Any
from framework.domain.domain_event import DomainEvent
from framework.domain.value_object import ValueObject
TId = TypeVar("TId", bound=ValueObject[Any])


class Entity(abc.ABC, Generic[TId]):
    id: TId = None
    events: List[DomainEvent] = []

    def __init__(self, entity_id: TId):
        self.id = entity_id

    def __eq__(self, other):
        if other is None:
            return False
        elif self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.id == other.id

    def __hash__(self) -> int:
        return hash(str(self.id))

    def add_domain_event(self, event: DomainEvent):
        self.events.append(event)

    def clear_events(self):
        self.events = []
