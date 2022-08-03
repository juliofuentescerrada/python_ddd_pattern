import unittest

from domain.model.address import Address
from domain.model.person import Person
from domain.model.person_id import PersonId


class EntityTests(unittest.TestCase):
    def test_entity(self):
        address = Address('Spain', 'Madrid', 'Móstoles', 'Osa Menor', 28938)
        myself = Person(PersonId('000001'), address)
        other_person = Person(PersonId('000001'), address)
        another_person = Person(PersonId('000002'), address)

        assert myself == other_person
        assert myself != another_person


if __name__ == '__main__':
    unittest.main()
