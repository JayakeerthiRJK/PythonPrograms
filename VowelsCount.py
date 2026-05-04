#Input
text = input("Enter a string: ")

#variables
vowel_count = 0
vowels = "aeiouAEIOU"

#Looping each character
for char in text:
    if char in vowels:
        vowel_count += 1

#print number of vowels
print("Number of vowels:", vowel_count)
