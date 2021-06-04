import unittest
from shoppingcart import ShoppingCart
from customer import Customer
from order import Order
from item import Item

class TestItem(unittest.TestCase):
    #set up an instance of the class
    def setUp(self):
        self.item = Item(name='Apple Watch',itemPrice=10, quantity=2, category='Electeronics')

    def test_price(self):
        self.assertEqual(self.item.itemPrice, 10)

    def test_name(self):
        self.assertEqual(self.item.name, 'Apple Watch')


    def test_category(self):
        self.assertEqual(self.item.category, 'Electeronics') 


    def test_item_price(self):
        self.assertEqual(self.item.itemPrice, 10) 







