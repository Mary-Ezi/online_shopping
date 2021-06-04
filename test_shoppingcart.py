import unittest
from shoppingcart import ShoppingCart
from item import Item

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        item1= Item(name='Apple AirPods',itemPrice=10, quantity=2, category='Electronics')
        item2= Item(name='Apple Watch', itemPrice=20, quantity=3, category='Electronics')
        item3= Item(name='Surface Laptop',itemPrice=30,quantity=4,category='Electronics')

        self.shopping_cart = ShoppingCart()
        self.shopping_cart.addItem(item1)
        self.shopping_cart.addItem(item2)
        self.shopping_cart.addItem(item3)

    def test_total_price(self):
        total_price = self.shopping_cart.getTotalPrice()
        self.assertEqual(total_price, 200)

    def test_add_item(self):
        item4 = Item(name='MacBook',itemPrice=10, quantity=2, category='Electronics')
        self.shopping_cart.addItem(item4)

        exist = False
        for item in self.shopping_cart.items:
            if item == item4:
                exist = True
        
        self.assertEqual(exist,True)


    
        

    def test_remove_item5(self):
        item5 = Item(name='iPhone 11',itemPrice=10, quantity=2, category='Electronics')
        self.shopping_cart.addItem(item5) 
        self.shopping_cart.removeItem(item5)

        exist = False
        for item in self.shopping_cart.items:
            if item == item5:
                exist = True

        self.assertEqual(exist,False)        






                

        
        




        