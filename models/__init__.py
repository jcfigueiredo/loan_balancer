class BaseModel(object):
    CONVERTERS = {}

    @classmethod
    def from_dict(cls, dict_):
        converted_dict = {}
        converters = cls.CONVERTERS
        for key, val in dict_.items():
            converter = converters.get(key)
            if converter:
                val = converter(val)
            converted_dict[key] = val

        # noinspection PyArgumentList
        return cls(**converted_dict)

    def __repr__(self) -> str:
        items = ('{}={!r}'.format(k, v) for k, v in self.__dict__.items())
        return "{}({})".format(self.__class__.__name__, ', '.join(items))


class Loan(BaseModel):
    CONVERTERS = {
        'id': int,
        'amount': int,
        'default_likelihood': float,
        'interest_rate': float,
    }

    # noinspection PyShadowingBuiltins
    def __init__(self, id, amount, default_likelihood, interest_rate, state) -> None:
        self.id = id
        self.amount = amount
        self.default_likelihood = default_likelihood
        self.interest_rate = interest_rate
        self.state = state

    def __eq__(self, o: object) -> bool:
        # noinspection PyUnresolvedReferences
        return self.id == o.id


class Facility(BaseModel):
    CONVERTERS = {
        'facility_id': int,
        'amount': int,
        'bank_id': float,
        'interest_rate': float,
    }

    def __init__(self, bank_id, facility_id, amount, interest_rate) -> None:
        self.bank_id = bank_id
        self.facility_id = facility_id
        self.interest_rate = interest_rate
        self.amount = amount

    def __eq__(self, o: object) -> bool:
        # noinspection PyUnresolvedReferences
        return self.facility_id == o.facility_id

class Bank(BaseModel):
    CONVERTERS = {
        'bank_id': int,
    }

    def __init__(self, bank_id, bank_name) -> None:
        self.bank_id = bank_id
        self.bank_name = bank_name

    def __eq__(self, o: object) -> bool:
        # noinspection PyUnresolvedReferences
        return self.bank_id == o.bank_id


class Covenant(BaseModel):
    CONVERTERS = {
        'facility_id': int,
        'bank_id': float,
        'max_default_likelihood': float,
    }

    def __init__(self, bank_id, facility_id, max_default_likelihood, banned_state) -> None:
        self.bank_id = bank_id
        self.facility_id = facility_id
        self.max_default_likelihood = max_default_likelihood
        self.banned_state = banned_state

    def __eq__(self, o: object) -> bool:
        # noinspection PyUnresolvedReferences
        return self.facility_id == o.facility_id and self.bank_id == o.bank_id \
               and self.max_default_likelihood == o.max_default_likelihood and self.banned_state == o.banned_state
