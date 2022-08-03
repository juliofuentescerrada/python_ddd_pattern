import abc
from typing import List, Any, TypeVar, Generic

T = TypeVar("T")


class ValueObject(abc.ABC, Generic[T]):
    value: T = None

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        elif self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            self_components = self.equality_members()
            other_components = other.equality_members()
            return self_components == other_components

    def __hash__(self) -> int:
        return hash(tuple(self.equality_members()))

    def __repr__(self) -> str:
        components = [str(c) for c in self.equality_members()]
        return f'{{ { ", ".join(components)} }}'

    @abc.abstractmethod
    def equality_members(self) -> List[Any]:
        pass
