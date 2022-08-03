import unittest
from domain.model.address import Address
from domain.model.email import Email


class ValueObjectTests(unittest.TestCase):
    def test_compound_value_object(self):
        my_address = Address('Spain', 'Madrid', 'Móstoles', 'Osa Menor', 28938)
        her_address = Address('Spain', 'Madrid', 'Móstoles', 'Osa Menor', 28938)
        their_address = Address('Spain', 'Madrid', 'Madrid', 'Via Lusitana', 28025)
        assert my_address == her_address
        assert my_address != their_address
        assert str(my_address) == '{ Spain, Madrid, Móstoles, Osa Menor, 28938 }'

    def test_simple_value_object(self):
        my_email = Email('julio@fuentes.com')
        my_other_email = Email('julio@fuentes.com')
        fake_email = Email('fake@fuentes.com')
        assert my_email == my_other_email
        assert my_email != fake_email
        assert str(my_email) == '{ julio@fuentes.com }'


if __name__ == '__main__':
    unittest.main()
