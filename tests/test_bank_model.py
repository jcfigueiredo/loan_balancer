import unittest

from models import Bank


# noinspection PyShadowingBuiltins
class TestBankModel(unittest.TestCase):
    def test_exists(self):
        id = 2
        name = 'Bank of America'
        bank = Bank(id=id, name=name)

        self.assertIsNotNone(bank)

        self.assertEqual(bank.id, id)
        self.assertEqual(bank.name, name)

    def test_is_equal_if_it_has_the_same_id(self):
        id = 1
        name = 'Bank of America'
        bank1 = Bank(id=id, name=name)
        bank2 = Bank(id=id, name=name)

        self.assertEqual(bank1, bank2)

    def test_is_not_equal_if_it_has_different_id(self):
        id = 1
        name = 'Bank of America'
        bank1 = Bank(id=id, name=name)
        bank2 = Bank(id=2, name=name)

        self.assertNotEqual(bank1, bank2)

    def test_can_be_created_from_dict(self):
        id = 2
        name = 'Bank of America'
        bank = Bank.from_dict({'id':  id, 'name': name})

        self.assertEqual(bank.id, id)
        self.assertEqual(bank.name, name)

    def test_can_be_created_from_dict_converting_properties(self):
        bank = Bank.from_dict({'id':  '2', 'name': 'Bank of America'})

        self.assertEqual(bank.id, 2)
        self.assertEqual(bank.name, 'Bank of America')

    def test_have_a_representation(self):
        bank = Bank.from_dict({'id':  '2', 'name': 'Bank of America'})
        self.assertEqual(bank.__repr__(), "Bank(id=2, name='Bank of America')")
