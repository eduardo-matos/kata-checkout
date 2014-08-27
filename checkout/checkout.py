# coding: utf-8

class Checkout(object):
    _price = 0

    def scan(self, item):
        if item == 'A':
            self.price += 50
        elif item == 'B':
            self.price += 30
        elif item == 'C':
            self.price += 20
        elif item == 'D':
            self.price += 15

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
