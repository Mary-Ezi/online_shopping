import datetime
from payment import Payment


class Order():

    def __init__(self, customer, shoppingCart):
        self.customer=customer
        self.shoppingcart = shoppingCart
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()
        

    def getcustomer(self):
        return self.customer 

    def getshoppingcart(self):
        return self.shoppingcart

    def setshoppingcart(self, shoppingcart):
        self.shoppingcart=shoppingcart 

    def getDate(self):
        return self.date 

    def getTime(self):
        return self.time  

    def place(self):
        totalPrice = self.shoppingcart.getTotalPrice()
        payment = Payment(totalPrice)
        payment.pay()
        return payment


