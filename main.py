from item import Item
from customer import Customer
from shoppingcart import ShoppingCart
from order import Order

def main():
    item1= Item(name='item1',itemPrice=10, quantity=2, category='A')
    item2= Item(name='item2', itemPrice=20, quantity=3, category='A')
    item3= Item(name='item3',itemPrice=30,quantity=4,category='B')

    shopping_cart = ShoppingCart()
    shopping_cart.addItem(item1)
    shopping_cart.addItem(item2)
    shopping_cart.addItem(item3)
    print(shopping_cart.getTotalPrice())
    print(shopping_cart.getTime())

    customer1 = Customer(phoneNumber='23456')
    order = Order(customer=customer1, shoppingCart= shopping_cart)
    payment = order.place()
    print(payment)

if __name__ == '__main__':
    main()




