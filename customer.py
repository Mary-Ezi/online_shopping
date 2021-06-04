class Customer:

    def __init__(self, id, name, email,phone):
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email

    def getphone(self):
        return self.phone

    def setphone(self, phone):
        self.phone=phone   
        