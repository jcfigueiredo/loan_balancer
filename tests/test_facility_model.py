import unittest

from models import Facility


class TestFacilityModel(unittest.TestCase):
    def test_exists(self):
        facility_id = 1
        bank_id = 2
        interest_rate = 0.07
        amount = 61104
        facility = Facility(bank_id=bank_id, facility_id=facility_id, amount=amount, interest_rate=interest_rate)

        self.assertIsNotNone(facility)

        self.assertEqual(facility.facility_id, facility_id)
        self.assertEqual(facility.bank_id, bank_id)
        self.assertEqual(facility.interest_rate, interest_rate)
        self.assertEqual(facility.amount, amount)

    def test_is_equal_if_it_has_the_same_id(self):
        facility_id = 1
        bank_id = 2
        interest_rate = 0.07
        amount = 61104
        facility1 = Facility(bank_id=bank_id, facility_id=facility_id, amount=amount, interest_rate=interest_rate)
        facility2 = Facility(bank_id=bank_id, facility_id=facility_id, amount=amount, interest_rate=interest_rate)

        self.assertEqual(facility1, facility2)

    def test_is_not_equal_if_it_has_different_id(self):
        facility_id = 1
        bank_id = 2
        interest_rate = 0.07
        amount = 61104
        facility1 = Facility(bank_id=bank_id, facility_id=facility_id, amount=amount, interest_rate=interest_rate)
        facility2 = Facility(bank_id=bank_id, facility_id=3, amount=amount, interest_rate=interest_rate)

        self.assertNotEqual(facility1, facility2)

    def test_can_be_created_from_dict(self):
        facility_id = 1
        bank_id = 2
        interest_rate = 0.07
        amount = 61104

        facility = Facility.from_dict({'interest_rate': 0.07, 'amount': 61104, 'facility_id': 1, 'bank_id': 2})

        self.assertEqual(facility.facility_id, facility_id)
        self.assertEqual(facility.bank_id, bank_id)
        self.assertEqual(facility.interest_rate, interest_rate)
        self.assertEqual(facility.amount, amount)

    def test_can_be_created_from_dict_converting_properties(self):
        facility = Facility.from_dict({'interest_rate': '0.07', 'amount': '61104', 'facility_id': '1', 'bank_id': '2'})

        self.assertEqual(facility.facility_id, 1)
        self.assertEqual(facility.bank_id, 2)
        self.assertEqual(facility.interest_rate, 0.07)
        self.assertEqual(facility.amount, 61104)

    def test_have_a_representation(self):
        facility = Facility.from_dict({'interest_rate': '0.07', 'amount': '61104', 'facility_id': '1', 'bank_id': '2'})
        self.assertEqual(facility.__repr__(), "Facility(bank_id=2.0, facility_id=1, interest_rate=0.07, amount=61104)")
