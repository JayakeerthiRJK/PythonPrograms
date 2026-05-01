def pass_req(password):
    if len(password) >= 8:
        has_number = any(char.isdigit() for char in password)
        if has_number:
            return "Password Created!"
        else:
            return "Password should contain number!"
    else:
        return "Password should be atleast 8 digits!"


password = input("Enter A Password: ")
print(pass_req(password))
