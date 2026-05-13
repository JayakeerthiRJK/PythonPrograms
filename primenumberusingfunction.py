def check_primenumber(n):
    if n <= 1:
        return "Not a prime number"
    for i in range(2,n+1):
        if n%i == 0:
            return"Not a prime number"
        else:
            return "It is a prime number"
        
 
n = int(input("Enter a number: "))

print(check_primenumber(n))
    
