#Variable for storing value
string = "RJK"
num = 12345

rev = ""
rev_num = 0

#Reversing String using loop

for ch in string:
    rev = ch+rev

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

print(rev)
print(rev_num)
