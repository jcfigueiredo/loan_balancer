import unittest

from models import Bank


class TestBankModel(unittest.TestCase):
    def test_exists(self):
        bank_id = 2
        bank_name = 'Bank of America'
        bank = Bank(bank_id=bank_id, bank_name=bank_name)

        self.assertIsNotNone(bank)

        self.assertEqual(bank.bank_id, bank_id)
        self.assertEqual(bank.bank_name, bank_name)

    def test_is_equal_if_it_has_the_same_id(self):
        bank_id = 1
        bank_name = 'Bank of America'
        bank1 = Bank(bank_id=bank_id, bank_name=bank_name)
        bank2 = Bank(bank_id=bank_id, bank_name=bank_name)

        self.assertEqual(bank1, bank2)

    def test_is_not_equal_if_it_has_different_id(self):
        bank_id = 1
        bank_name = 'Bank of America'
        bank1 = Bank(bank_id=bank_id, bank_name=bank_name)
        bank2 = Bank(bank_id=2, bank_name=bank_name)

        self.assertNotEqual(bank1, bank2)

    def test_can_be_created_from_dict(self):
        bank_id = 2
        bank_name = 'Bank of America'
        bank = Bank.from_dict({'bank_id':  bank_id, 'bank_name': bank_name})

        self.assertEqual(bank.bank_id, bank_id)
        self.assertEqual(bank.bank_name, bank_name)

    def test_can_be_created_from_dict_converting_properties(self):
        bank = Bank.from_dict({'bank_id':  '2', 'bank_name': 'Bank of America'})

        self.assertEqual(bank.bank_id, 2)
        self.assertEqual(bank.bank_name, 'Bank of America')

    def test_have_a_representation(self):
        bank = Bank.from_dict({'bank_id':  '2', 'bank_name': 'Bank of America'})
        self.assertEqual(bank.__repr__(), "Bank(bank_id=2, bank_name='Bank of America')")
