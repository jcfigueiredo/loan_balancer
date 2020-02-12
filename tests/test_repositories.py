import unittest

from models import Loan, Bank, Covenant, Facility
from repositories import LoanRepository, BankRepository, CovenantRepository, FacilityRepository


class TheLoanRepository(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = LoanRepository()

    def test_exists(self):
        self.assertIsNotNone(self.repo)

    def test_loads_from_files(self):
        expected_loans = [Loan(id=1, amount=10552, default_likelihood=0.02, interest_rate=0.15, state='MO'),
                          Loan(id=2, amount=51157, default_likelihood=0.01, interest_rate=0.15, state='VT'),
                          Loan(id=3, amount=74965, default_likelihood=0.06, interest_rate=0.35, state='AL')]

        loans = LoanRepository.load_from_file(path='./tests/fixtures/loans.csv')

        self.assertListEqual(loans, expected_loans)


class TheBankRepository(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = BankRepository()

    def test_exists(self):
        self.assertIsNotNone(self.repo)

    def test_loads_from_files(self):
        expected_banks = [Bank(id=1, name='Chase'), Bank(id=2, name='Bank of America')]

        loans = BankRepository.load_from_file(path='./tests/fixtures/banks.csv')

        self.assertListEqual(loans, expected_banks)


class TheCovenantRepository(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = CovenantRepository()

    def test_exists(self):
        self.assertIsNotNone(self.repo)

    def test_loads_from_files(self):
        expected_covenants = [Covenant(bank_id=1.0, facility_id=2, max_default_likelihood=0.09, banned_state='MT'),
                              Covenant(bank_id=2.0, facility_id=1, max_default_likelihood=0.06, banned_state='VT'),
                              Covenant(bank_id=2.0, facility_id=1, max_default_likelihood=None, banned_state='CA')]

        covenants = CovenantRepository.load_from_file(path='./tests/fixtures/covenants.csv')

        self.assertListEqual(covenants, expected_covenants)


class TheFacilitiesRepository(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = FacilityRepository()

    def test_exists(self):
        self.assertIsNotNone(self.repo)

    def test_loads_from_files(self):
        expected_facilities = [Facility(bank_id=1, id=2, interest_rate=0.07, amount=61104),
                               Facility(bank_id=2, id=1, interest_rate=0.06, amount=126122)]

        facilities = FacilityRepository.load_from_file(path='./tests/fixtures/facilities.csv')

        self.assertListEqual(facilities, expected_facilities)
