from domain.model.person import Person
from domain.model.person_id import PersonId
from framework.domain.repository import Repository


class PersonRepository(Repository[PersonId, Person]):
    data = {}

    def find(self, entity_id: PersonId) -> Person:
        return self.data[entity_id]

    def save(self, entity: Person) -> None:
        self.data[entity.id] = entity
