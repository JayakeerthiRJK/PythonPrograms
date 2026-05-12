# PasswordChecker class 
class PasswordChecker:
    # Initialize the class with a password
    def __init__(self, password):
        self.password = password

    # Method to check if the password is strong 
    def is_strong(self):
        # Check if the password meets the criteria for a strong password
        if len(self.password) < 8:
            return "Password must be at least 8 characters long."
        # Check for uppercase, lowercase, digit, and special character
        if not any(char.isupper() for char in self.password):
            return "Password must contain at least one uppercase letter."
        # Check for lowercase letter
        if not any(char.islower() for char in self.password):
            return "Password must contain at least one lowercase letter."   
        # Check for digit
        if not any(char.isdigit() for char in self.password):
            return "Password must contain at least one digit."
        # Check for special character
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in self.password):
            return "Password must contain at least one special character."
        # If all criteria are met, return that the password is strong
        return "Password is strong."
    
# Example usage of the PasswordChecker class
password1 = PasswordChecker("Password123!")
password2 = PasswordChecker("weakpass")
password3 = PasswordChecker("NoSpecialChar1")
password4 = PasswordChecker("Short1!")
# Check the strength of the passwords
print(password1.is_strong())
print(password2.is_strong())
print(password3.is_strong())
print(password4.is_strong())