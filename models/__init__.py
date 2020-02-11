class Loan(object):
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

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)
