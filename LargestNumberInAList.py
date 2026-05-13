def largest_value():
    num = []
    large = 0
    print(num)
    num_of_element = int(input("Enter the number of element to add in the list: "))
    for i in range(num_of_element):
        element = int(input(f"Enter the value for element {i}: "))
        num.append(element)
    print(num)

    for i in num:
        if i > large:
            large = i
    print(large)

largest_value()
