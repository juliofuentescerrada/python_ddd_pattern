from typing import List, Any
from framework.domain.value_object import ValueObject


class Email(ValueObject[str]):
    def __init__(self, address: str):
        self.value = address

    def equality_members(self) -> List[Any]:
        return [self.value]

