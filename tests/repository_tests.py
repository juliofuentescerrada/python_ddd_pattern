import unittest

from domain.model.address import Address
from domain.model.person import Person
from domain.model.person_id import PersonId
from domain.repositories.person_repository import PersonRepository


class RepositoryTests(unittest.TestCase):
    def test_repositories(self):
        person = Person.create(PersonId('000001'), Address('Spain', 'Madrid', 'Móstoles', 'Osa Menor', 28938))

        repo = PersonRepository()
        repo.save(person)

        me = repo.find(person.id)
        assert me is not None
        assert me == person


if __name__ == '__main__':
    unittest.main()
