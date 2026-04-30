def total_bill(price,quantity):
    return price*quantity

item = input("Enter the item name: ")
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

print("Total Bill: ",total_bill(price,quantity))
