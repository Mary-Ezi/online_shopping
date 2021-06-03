from item import Item
from payment import Payment
import datetime

class ShoppingCart():

    def __init__(self):
        self.items = []
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def getItemId(self):
        return self.id
    
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def getDate(self):
        return self.date 

    def getTime(self):
        return self.time  

    def getTotalPrice(self):
        total = 0
        for item in self.items:
            total += item.getItemPrice() * item.quantity
        return total

 



           