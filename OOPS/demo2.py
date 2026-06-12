'''
If students need to implement OOP concepts themselves, give projects where overloading, overriding, constructors, inheritance, etc. are naturally required.

1. Food Delivery App 

Classes:

User
Restaurant
Order
Concepts:

Constructor → create user/order
Overriding → calculate_bill()
Normal Order
Premium Order
Overloading → add_item()
by item name
by item name + quantity
'''
#Food delivery app 
from multipledispatch import dispatch
class User:
    def __init__(self, name):
        self.name = name
class Restaurant:
    def __init__(self, name):
        self.name = name
class Order:
    def __init__(self, user, restaurant):
        self.user = user
        self.restaurant = restaurant
        self.items = []
    
    @dispatch(str)
    def add_item(self, item):
        self.items.append(item)

    @dispatch(str, int)
    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def calculate_bill(self):
        bill = 0 
        count = 0
        for item in self.items:
            if isinstance(item, str):
                bill += 10  # Assuming each item costs $10
            elif isinstance(item, tuple):
                bill += 10 * item[1]  # Quantity * price
        return bill 


# Example usage
user1 = User("Alice")
restaurant1 = Restaurant("Pizza Place")
order1 = Order(user1, restaurant1)
order1.add_item("Pizza")
order1.add_item("Burger", 2)
print(f"Total bill for {user1.name} at {restaurant1.name}: ${order1.calculate_bill()}")