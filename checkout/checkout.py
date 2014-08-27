# coding: utf-8

from collections import OrderedDict


item_prices_one = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

item_prices_two = {
    'BB': 45,
}

item_prices_three = {
    'AAA': 130,
}


class PriceRules(object):

    def __init__(self):
        self._rules = {}

    def add_rule(self, item, price, quantity=1):
        if len(item) > 1:
            raise ValueError('Item name must have 1 character only')

        if quantity not in self._rules:
            self._rules[quantity] = {}

        self._rules[quantity][item] = price

    @property
    def rules(self):
        return OrderedDict(sorted(self._rules.items()))


class Checkout(object):
    items = ''

    def scan(self, item):
        self.items += item

    @property
    def price(self):
        self.items = ''.join(sorted(self.items))

        combo_3 = self._compute_combos(item_prices_three)
        combo_2 = self._compute_combos(item_prices_two)
        combo_1 = self._compute_combos(item_prices_one)

        return combo_3 + combo_2 + combo_1

    def _compute_combos(self, combos):
        _price = 0

        for combo, val in combos.iteritems():
            if combo in self.items:
                _price += self.items.count(combo) * val
                self.items = self.items.replace(combo, '')

        return _price
