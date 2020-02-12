import csv

from models import Loan, Bank, Covenant, Facility


class BaseRepository(object):
    MODEL = None

    @classmethod
    def load_from_file(cls, path):
        items = []
        f = open(path, 'rt')
        try:
            reader = csv.DictReader(f)
            for row in reader:
                items.append(cls.MODEL.from_dict(row))
        finally:
            f.close()
        return items


class LoanRepository(BaseRepository):
    MODEL = Loan


class BankRepository(BaseRepository):
    MODEL = Bank


class CovenantRepository(BaseRepository):
    MODEL = Covenant


class FacilityRepository(BaseRepository):
    MODEL = Facility
