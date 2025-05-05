import Modules.CheckPassReq
import Modules.GeneratePass

class Registration():
    def __init__(self,LoggedIn):
        self.LoggedIn = LoggedIn
        #Get username
        if LoggedIn:
            self.account = input("Enter the account name: ")
            self.category = input("Enter the category you want to put this in: ")
        else:
            self.userName = input("Enter your username: ")
        #Get password
        print("\nPassword must contain:\n\tAtleast 1 special character\n\tAtleast 1 number\n\tAtleast 8 characters\n")
        self.password = input("Enter a password Or enter 'n' to generate a password: ") #TODO- Me: ADD PASSWORD GENERATOR
        # print(f"Initial password: {self.password}")#for DEBUG
        self.makePassword(self.password)
        
        #Get name
        if not LoggedIn:
            firstName = input("Enter your first name: ").title
            lastName = input("Enter your last name: ").title
            if lastName != None:
                self.store()
        else:
            if self.hint != None:
                self.store()
    def makePassword(self,InitialPassword):

        if InitialPassword != "n" or InitialPassword != "N":
            password = InitialPassword
            #Verification of password and allowing reinput
            while not self.verify(password)[0]:
                print(self.verify(password)[1])
                password = input("Enter a new password: ")
                print(f"New password: {password}")#for DEBUG
            #Password encryption
            if self.verify(password)[0]:
                self.password = password
                self.password = self.encrypt(self.password)
                print(f"Encrypted password: {self.password}") #for DEBUG
            #Create hint
            self.hint = input("Enter a hint for if you forget your password: ")
            print(f"Hint: '{self.hint}'")
        else:
            self.password = Modules.GeneratePass.Generate()

    def verify(self,password):
        requirement = Modules.CheckPassReq.Check()
        return requirement.isValid(password)
    
    def encrypt(self,password):
        #Very sick encryption
        password += "a"

        return f"{password}a"
    
    def store(self):
        if self.LoggedIn:
            self.category = input("What category would you like to store this in? ")
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/Password.txt (Contains encrypted password in file)
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/First.txt (Contains Firstname in file) 
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/Last.txt  (Contains Lastname in file)
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/Hint.txt  (Contains Password hint in file)
            return True
        else:
            #TODO: Add a way to create DataStorage/{self.username}/Accounts
            #TODO: Add a way to store DataStorage/{self.username}/User/Password.txt (Contains encrypted password in file)
            #TODO: Add a way to store DataStorage/{self.username}/User/First.txt (Contains Firstname in file) 
            #TODO: Add a way to store DataStorage/{self.username}/User/Last.txt  (Contains Lastname in file)
            #TODO: Add a way to store DataStorage/{self.username}/User/Hint.txt  (Contains Password hint in file)
            return True