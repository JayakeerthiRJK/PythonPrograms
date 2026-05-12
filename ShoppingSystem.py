# Shopping System using OOP
class shoppingSystem:
    # Initialize the shopping system with an empty cart
    def __init__(self):
        self.cart = []
    
    # Method to add items to the cart
    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        print(f"{item} has been added to your cart.")
    
    # Method to view items in the cart
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item, price in self.cart:
                print(f"- {item}: ${price}")


    # Method to calculate the total cost of items in the cart
    def calculate_total(self):
        total = 0
        for item, price in self.cart:
            total += price
        print(f"Total amount: ${total}")

    # Method to apply a discount to the total cost
    def discount(self, percentage):
        # Calculate the total cost first
        total = 0
        for item, price in self.cart:
            total += price
        # Calculate the discount amount and the discounted total
        discount_amount = total * (percentage / 100)
        discounted_total = total - discount_amount
        print(f"Total after {percentage}% discount: ${discounted_total}")


#object creation and method calls 
shopping = shoppingSystem()
# Adding items to the cart
shopping.add_to_cart("Laptop", 1000)
shopping.add_to_cart("Smartphone", 500)
# Viewing the cart
shopping.view_cart()
# Calculating the total cost
shopping.calculate_total()
# applying a 10% discount to the total cost
shopping.discount(10) 