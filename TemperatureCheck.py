#check wether water is hot,cold or normal using function
def temp_cal(temp):
    if temp > 30:
        return "Water is hot!"
    elif temp < 15:
        return "Water is cold!"
    else:
        return "Normal"


#temperature input
temp = int(input("Enter the temperature: "))

#using function to compare temperature
print(temp_cal(temp))
