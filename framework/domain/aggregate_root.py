from typing import TypeVar, Any
from framework.domain.entity import Entity
from framework.domain.value_object import ValueObject
TId = TypeVar("TId", bound=ValueObject[Any])


class AggregateRoot(Entity[TId]):
    pass
