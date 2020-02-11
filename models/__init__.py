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
        converted_dict = {}
        converters = {
            'id': int,
            'amount': int,
            'default_likelihood': float,
            'interest_rate': float,
        }
        for key, val in dict_.items():
            converter = converters.get(key)
            if converter:
                val = converter(val)
            converted_dict[key] = val

        return cls(**converted_dict)

    def __repr__(self) -> str:
        items = ('{}={!r}'.format(k, v) for k, v in self.__dict__.items())
        return "{}({})".format(self.__class__.__name__, ', '.join(items))



