from domain.events.person_created import PersonCreated
from domain.events.person_deleted import PersonDeleted
from domain.events.person_updated import PersonUpdated
from domain.model.address import Address
from domain.model.person_id import PersonId
from framework.domain.aggregate_root import AggregateRoot


class Person(AggregateRoot[PersonId]):
    _address: Address = None

    def __init__(self, entity_id: PersonId, address: Address):
        super().__init__(entity_id)
        self._address = address

    @staticmethod
    def create(entity_id: PersonId, address: Address):
        person = Person(entity_id, address)
        person.add_domain_event(PersonCreated(person.id, person._address))
        return person

    def change_address(self, address: Address):
        self._address = address
        self.add_domain_event(PersonUpdated(self.id, self._address))

    def deactivate(self):
        self.add_domain_event(PersonDeleted(self.id))


