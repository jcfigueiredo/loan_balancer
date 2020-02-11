import csv
import unittest

from models import Loan


class LoanRepository(object):

    @classmethod
    def load_from_file(cls, path):
        loans = []
        f = open(path, 'rt')
        try:
            reader = csv.DictReader(f)
            for row in reader:
                Loan.from_dict(row)
        finally:
            f.close()
        return loans


class TheLoanRepository(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repo = LoanRepository()

    def test_exists(self):
        self.assertIsNotNone(self.repo)

    def test_loads_from_files(self):
        loans = LoanRepository.load_from_file(path='./tests/fixtures/loans.csv')

        self.assertListEqual(loans, [])

