import unittest

from models import Covenant


class TestCovenantModel(unittest.TestCase):
    def test_exists(self):
        facility_id = 1
        bank_id = 2

        max_default_likelihood = 12
        banned_state = 'MT'
        covenant = Covenant(bank_id=bank_id, facility_id=facility_id, max_default_likelihood=max_default_likelihood,
                            banned_state=banned_state)

        self.assertIsNotNone(covenant)

        self.assertEqual(covenant.facility_id, facility_id)
        self.assertEqual(covenant.bank_id, bank_id)
        self.assertEqual(covenant.banned_state, banned_state)
        self.assertEqual(covenant.max_default_likelihood, max_default_likelihood)

    def test_is_equal_if_it_all_fields_are_the_same(self):
        facility_id = 1
        bank_id = 2
        max_default_likelihood = 12
        banned_state = 'MT'
        covenant1 = Covenant(bank_id=bank_id, facility_id=facility_id, max_default_likelihood=max_default_likelihood,
                             banned_state=banned_state)
        covenant2 = Covenant(bank_id=bank_id, facility_id=facility_id, max_default_likelihood=max_default_likelihood,
                             banned_state=banned_state)

        self.assertEqual(covenant1, covenant2)

    def test_is_not_equal_if_any_field_is_different(self):
        facility_id = 1
        bank_id = 2
        max_default_likelihood = 12
        banned_state = 'MT'
        covenant1 = Covenant(bank_id=bank_id, facility_id=facility_id, max_default_likelihood=max_default_likelihood,
                             banned_state=banned_state)
        covenant2 = Covenant(bank_id=bank_id, facility_id=2, max_default_likelihood=max_default_likelihood,
                             banned_state=banned_state)
        covenant3 = Covenant(bank_id=4, facility_id=2, max_default_likelihood=max_default_likelihood,
                             banned_state=banned_state)

        self.assertNotEqual(covenant1, covenant2)
        self.assertNotEqual(covenant2, covenant3)

    def test_can_be_created_from_dict(self):
        facility_id = 1
        bank_id = 2
        max_default_likelihood = 12
        banned_state = 'MT'

        covenant = Covenant.from_dict({'max_default_likelihood': 12, 'banned_state': 'MT', 'facility_id': 1,
                                       'bank_id': 2})

        self.assertEqual(covenant.facility_id, facility_id)
        self.assertEqual(covenant.bank_id, bank_id)
        self.assertEqual(covenant.banned_state, banned_state)
        self.assertEqual(covenant.max_default_likelihood, max_default_likelihood)

    def test_can_be_created_from_dict_converting_properties(self):
        facility_id = 1
        bank_id = 2
        max_default_likelihood = 1.2
        banned_state = 'MT'

        covenant = Covenant.from_dict({'max_default_likelihood': '1.2', 'banned_state': 'MT', 'facility_id': '1',
                                       'bank_id': '2'})

        self.assertEqual(covenant.facility_id, facility_id)
        self.assertEqual(covenant.bank_id, bank_id)
        self.assertEqual(covenant.banned_state, banned_state)
        self.assertEqual(covenant.max_default_likelihood, max_default_likelihood)

    def test_can_handle_empty_max_default(self):
        facility_id = 1
        bank_id = 2
        max_default_likelihood = None
        banned_state = 'MT'

        covenant = Covenant.from_dict({'max_default_likelihood': '', 'banned_state': 'MT', 'facility_id': '1',
                                       'bank_id': '2'})

        self.assertEqual(covenant.facility_id, facility_id)
        self.assertEqual(covenant.bank_id, bank_id)
        self.assertEqual(covenant.banned_state, banned_state)
        self.assertEqual(covenant.max_default_likelihood, max_default_likelihood)

    def test_have_a_representation(self):
        covenant = Covenant.from_dict({'max_default_likelihood': '1.2', 'banned_state': 'MT', 'facility_id': '1',
                                       'bank_id': '2'})
        self.assertEqual(covenant.__repr__(), "Covenant(bank_id=2.0, facility_id=1, max_default_likelihood=1.2, "
                                              "banned_state='MT')")
