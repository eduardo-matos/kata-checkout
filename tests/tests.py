import unittest
from checkout.checkout import Checkout


__all__ = ['CheckoutTest']


class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.co = Checkout()

    def test_no_item_returns_zero(self):
        self.co.scan('')
        self.assertEqual(0, self.co.price)

    def test_can_check_one_item(self):
        self.co.scan('A')
        self.assertEqual(50, self.co.price)

    def test_can_check_multiple_distinct_items(self):
        self.co.scan('A')
        self.co.scan('B')
        self.co.scan('C')
        self.co.scan('D')
        self.assertEqual(115, self.co.price)

    def test_can_deal_with_discounts(self):
        self.co.scan('A')
        self.co.scan('A')
        self.co.scan('A')
        self.assertEqual(130, self.co.price)
