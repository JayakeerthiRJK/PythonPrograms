#Getting Input For Withdraw Amount
withdraw_amount = int(input("Enter the amount to withdraw: "))

#Users Balance
bal = 55000

#Using if condition to check users balance
if withdraw_amount > bal:
    print("Insufficient Balance!")
    print("Your Balance: ",bal)
else:
    print(f"Withdrawal of the amount {withdraw_amount} successfull!")
    #minus the withdraw amount from the balance
    bal = bal - withdraw_amount
    print("Your Balance: ",bal)

