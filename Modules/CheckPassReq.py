import string

class Check(): # Checks the password requirements
    def __init__(self):
        self.allowedSpecialChars = string.punctuation
        self.allowedChars = string.ascii_letters + string.digits + string.punctuation
    def isValid(self, password):
        if len(password) < 8:
            return False,f"Password must be atleast 8 characters long."
        if len(password) > 100:
            return False,f"Pasword must be less than 100 characters long."
        if not(any(char in string.ascii_uppercase for char in password)):  # Check for uppercase
            return False,f"Password must contain atleast 1 uppercase letter."
        if not(any(char in string.digits for char in password)): # Check for a num
            return False,f"Password must contain atleast 1 number."
        if not(any(char in string.punctuation for char in password)): # Check for special
            return False,f"Password must contain atleast 1 special character."
        for char in password:
            if char not in self.allowedChars:
                return False,f"Password cannot contain '{char}'"
        return True,"Password accepted"
#DONE