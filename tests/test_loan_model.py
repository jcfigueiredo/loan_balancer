import unittest

from models import Loan


class TestLoanModel(unittest.TestCase):
    def test_exists(self):
        state = 'MO'
        interest_rate = 0.15
        default_likelihood = 0.02
        amount = 10552
        id_ = 1
        loan = Loan(id=id_, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                    state=state)

        self.assertIsNotNone(loan)

        self.assertEqual(loan.id, id_)
        self.assertEqual(loan.amount, amount)
        self.assertEqual(loan.default_likelihood, default_likelihood)
        self.assertEqual(loan.interest_rate, interest_rate)
        self.assertEqual(loan.state, state)

    def test_is_equal_if_it_has_the_same_id(self):
        state = 'NY'
        interest_rate = 0.12
        default_likelihood = 0.22
        amount = 10532
        id_ = 2

        loan1 = Loan(id=id_, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                     state=state)
        loan2 = Loan(id=id_, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                     state=state)

        self.assertEqual(loan1, loan2)

    def test_is_not_equal_if_it_has_different_id(self):
        state = 'CT'
        interest_rate = 0.21
        default_likelihood = 0.12
        amount = 10456
        id_ = 3

        loan1 = Loan(id=id_, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                     state=state)
        loan2 = Loan(id=4, amount=amount, default_likelihood=default_likelihood, interest_rate=interest_rate,
                     state=state)

        self.assertNotEqual(loan1, loan2)

    def test_can_be_created_from_dict(self):
        loan = Loan.from_dict({'interest_rate': 0.15, 'amount': 10552, 'id': 1, 'default_likelihood': 0.02,
                               'state': 'MO'})

        self.assertEqual(loan.id, 1)
        self.assertEqual(loan.amount, 10552)
        self.assertEqual(loan.default_likelihood, 0.02)
        self.assertEqual(loan.interest_rate, 0.15)
        self.assertEqual(loan.state, 'MO')

    def test_can_be_created_from_dict_converting_properties(self):
        loan = Loan.from_dict({'interest_rate': '0.15', 'amount': '10552', 'id': '1', 'default_likelihood': '0.02',
                               'state': 'MO'})

        self.assertEqual(loan.id, 1)
        self.assertEqual(loan.amount, 10552)
        self.assertEqual(loan.default_likelihood, 0.02)
        self.assertEqual(loan.interest_rate, 0.15)
        self.assertEqual(loan.state, 'MO')
