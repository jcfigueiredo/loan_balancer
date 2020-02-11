import unittest


class Loan(object):
    def __init__(self, id_, amount, default_likelihood, interest_rate, state) -> None:
        self.id = id_
        self.amount = amount
        self.default_likelihood = default_likelihood
        self.interest_rate = interest_rate
        self.state = state


class TestLoanModel(unittest.TestCase):
    def test_exists(self):
        state = 'MO'
        interest_rate = 0.15
        default_likelihood = 0.02
        amount = 10552
        id_ = 1
        loan = Loan(id_=id_, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                    state=state)

        self.assertIsNotNone(loan)

        self.assertEqual(loan.id, id_)
        self.assertEqual(loan.amount, amount)
        self.assertEqual(loan.default_likelihood, default_likelihood)
        self.assertEqual(loan.interest_rate, interest_rate)
        self.assertEqual(loan.state, state)



if __name__ == '__main__':
    unittest.main()
