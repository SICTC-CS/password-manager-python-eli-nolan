from Modules.Register import Registration
import hashlib
from Modules.GeneratePass import Generate
# Log in to run the program:

class Run:
    def __init__(self):
        print("Running LOGIN")
         
    def Login(self):    #Used for logging the user in
        firstTime = input("Are you a first time user? (y/n): ")
        if (firstTime in ["y","Y","Yes","yes"]): #Determine if the user said yes
            self.firstTime = True
        else:
            self.firstTime = False
                
        if self.firstTime: # if they are first time user have them register
            reg = Registration(False)
            if reg:
                print("Registration complete.")
            else:
                print("There was an error with registration... please try again later.")
                exit()
                
        failedAttempts = 0
        userName = input("Please enter your username: ")
        password = self.Check(input("Enter your password: "),userName)
        while not password:
            failedAttempts += 1
            if failedAttempts <3: 
                print(f"Incorrect password {3-failedAttempts} attempts left...")
                print(f"Hint: {self.checkHint(userName)}")
                password = self.Check(input("Enter your password: "),userName)
            else: #3 fails and return false
                return False,userName
        return True,userName
        
    def Check(self,password,user): #For checking if the password matches the stored password
        actual = self.getPass(user)
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == actual: #Check hash with stored hash seems to be the typical way to do this
            return True
        else:
            return False    
    
    def checkHint(self,user): #For checking for a hint or account
        try:
            with open(f"Modules/DataStorage/{user}/User/Hint.txt", "r") as f:
                hint = f.read().strip()
            f.close()
            return (hint)
        except FileNotFoundError:
            return f"Account not found for {user}"
        
    def getPass(self,user): #Grabs the encrypted password from file 
        try:
            with open(f"Modules/DataStorage/{user}/User/Password.txt", "r") as f:
                password = f.read().strip()
            f.close()
            return (password)
        except FileNotFoundError:
            return f"Account not found for {user}"+Generate() #Secured a Vulnerability, If you type the user as a for a non existant account you could just use that as the password and it would work