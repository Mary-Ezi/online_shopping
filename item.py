class Item():

    def __init__(self, name, itemPrice, quantity, category):
        self.name = name
        self.itemPrice = itemPrice
        self.quantity=quantity
        self.category = category
    
    def getItemName(self):
        return self.name

    def setItemName(self, name):
        self.name = name 

    def getQuantity(self):
        return self.quantity      
    
    def getItemPrice(self):
        return self.itemPrice 

    def setItemPrice(self, itemPrice):
        self.itemPrice = itemPrice           
    
    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category    

    
    def __str__(self):
        return self.name + ' ' + str(self.itemPrice)


