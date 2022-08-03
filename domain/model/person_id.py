from typing import List, Any

from framework.domain.value_object import ValueObject


class PersonId(ValueObject[str]):
    def __init__(self, value: str):
        self.value = value

    def equality_members(self) -> List[Any]:
        return [self.value]


