a = []

for i in range(10):
    element = int(input(f"Enter the value for element {i+1}:"))
    a.append(element)
print("Array: ",a)
print("Even Numbers:")
for i in range(10):
    if a[i] % 2 == 0:
        print(a[i])
