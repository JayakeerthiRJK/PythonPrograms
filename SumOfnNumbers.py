#input
n = int(input("Enter a number: "))

#variable
total = 0

#loop from 1 to n and adding
for i in range(1, n + 1):
    print(i)    
    total += i        

#print total
print("Sum =", total)
