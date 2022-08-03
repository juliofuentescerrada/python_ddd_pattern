from domain.model.address import Address
from domain.model.person_id import PersonId
from framework.domain.domain_event import DomainEvent


class PersonCreated(DomainEvent):
    def __init__(self, person_id: PersonId, address: Address):
        self.person_id = person_id.value
        self.country = address.value.country
        self.state = address.value.state
        self.city = address.value.city
        self.street = address.value.street
        self.zip_no = address.value.zip_no
