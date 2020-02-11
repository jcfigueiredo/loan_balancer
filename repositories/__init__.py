import csv

from models import Loan


class LoanRepository(object):

    @classmethod
    def load_from_file(cls, path):
        loans = []
        f = open(path, 'rt')
        try:
            reader = csv.DictReader(f)
            for row in reader:
                loans.append(Loan.from_dict(row))
        finally:
            f.close()
        return loans