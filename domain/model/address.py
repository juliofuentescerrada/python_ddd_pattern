import dataclasses
from typing import List, Any
from framework.domain.value_object import ValueObject


@dataclasses.dataclass
class AddressValue:
    country: str = None
    state: str = None
    city: str = None
    street: str = None
    zip_no: int = None


class Address(ValueObject[AddressValue]):
    def __init__(self, country: str, state: str, city: str, street: str, zip_no: int):
        self.value = AddressValue(country, state, city, street, zip_no)

    def equality_members(self) -> List[Any]:
        return [
            self.value.country,
            self.value.state,
            self.value.city,
            self.value.street,
            self.value.zip_no,
        ]
