def count_vowels(string):
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            print(char)

x = input("Enter a String: ")

count_vowels(x)
        
