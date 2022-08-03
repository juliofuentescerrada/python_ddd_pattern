from domain.model.person_id import PersonId
from framework.domain.domain_event import DomainEvent


class PersonDeleted(DomainEvent):
    def __init__(self, person_id: PersonId):
        self.person_id = person_id.value
