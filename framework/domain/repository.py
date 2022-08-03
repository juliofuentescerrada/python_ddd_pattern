import abc
from typing import TypeVar, Generic, Any

from framework.domain.aggregate_root import AggregateRoot
from framework.domain.value_object import ValueObject

TId = TypeVar("TId", bound=ValueObject[Any])
TAggregateRoot = TypeVar("TAggregateRoot", bound=AggregateRoot)


class Repository(abc.ABC, Generic[TId, TAggregateRoot]):
    @abc.abstractmethod
    def find(self, entity_id: TId) -> TAggregateRoot:
        pass

    @abc.abstractmethod
    def save(self, entity: TAggregateRoot) -> None:
        pass
