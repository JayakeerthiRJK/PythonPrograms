print("Product Details")
name = input("Enter the product name: ")
price = float(input(f"Enter the price for the product {name}: "))
quantity = int(input("Enter the quantity: "))
discount = int(input("Enter the discount percentage: "))
final_bill = price - (price*discount)/100 
print(f"The final bill is {final_bill}")
