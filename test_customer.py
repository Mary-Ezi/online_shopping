import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.item = Customer(id=133,name ='Jen Smith', email='jen@gmail.com',phone='2065121172')

    def test_phone_number(self):
        self.assertEqual(self.item.phone,'2065121172')

    def test_id(self):
        self.assertEqual(self.item.id,133) 

    def test_email(self):
        self.assertEqual(self.item.email,'jen@gmail.com')        
 



