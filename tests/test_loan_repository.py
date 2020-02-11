import unittest

from models import Loan
from repositories import LoanRepository


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
