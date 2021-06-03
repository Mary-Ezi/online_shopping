class Payment():
    
    def __init__(self, payment_amount):
        self.payment_amount = payment_amount
        self.payment_status = None
    
    def pay(self):
        # to be implemented
        # if payement is successful return True unless return False
        self.payment_status = True
    
    def __str__(self):
        if self.payment_status:
            return "You have paid $" + str(self.payment_amount)
        else:
            return "Order was not successful!"