import Modules.CheckPassReq
import Modules.GeneratePass
import hashlib
import os

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
        self.password = input("Enter a master password Or enter 'n' to generate a master password: ")
        self.makePassword(self.password)
        # print(f"Initial password: {self.password}")#for DEBUG
        #Get name
        if not LoggedIn:
            self.firstName = input("Enter your first name: ").title
            self.lastName = input("Enter your last name: ").title
            if self.lastName != None:
                self.store()
        else:
            if self.hint != None:
                self.store()
    def makePassword(self,InitialPassword):
        if InitialPassword != "n":
            password = InitialPassword
            #Verification of password and allowing reinput
            while not self.verify(password)[0]:
                print(self.verify(password)[1])
                if not self.LoggedIn:
                    password = input("Enter a new Master password: ")
                else:
                    password = input("Enter a new password: ")
                
            #Password encryption
            if self.verify(password)[0]:
                if not self.LoggedIn:
                    self.password = self.encrypt(password)
                else:
                    self.password = self.encode(password)
                # print(f"Encrypted password: {self.password}") #for DEBUG
            #Create hint
            if self.LoggedIn == False:
                self.hint = input("Enter a hint for if you forget your master password: ")
                print(f"Hint: '{self.hint}'")
        else:
            Generator = Modules.GeneratePass.Generate()
            password = Generator.Gen()
            self.password = self.encrypt(password)
            print(f"Generated master password: {password}")
            # print(f"DEBUG Encrypted password: {self.password}") #for DEBUG

            self.hint = "Randomly generated password..."
            
    def verify(self,password):
        requirement = Modules.CheckPassReq.Check()
        return requirement.isValid(password)
    
    def encrypt(self,password):
        print(hashlib.sha256(password.encode('utf-8')).hexdigest()) #DEBUG
        return hashlib.sha256(password.encode('utf-8')).hexdigest() #This encrypts the password as a byte and sets it to 32 in length from what i understand 

    def store(self):
        path = f"Modules/DataStorage"
        if self.LoggedIn:
            self.category = input("What category would you like to store this in? ")
            
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/Password.txt (Contains encrypted password in file)
            #TODO: Add a way to store DataStorage/{self.username}/Accounts/{self.category}/{self.account}/Hint.txt  (Contains Password hint in file)
            
            return True
        else:
            os.makedirs(f"{path}/{self.userName}/User",exist_ok=True) #Create the path down to /user 
            accountPath = f"{path}/{self.userName}/User" 
            
            with open (f"{accountPath}/Password.txt", "w+") as f: #make password.txt
                f.write(self.password)
            with open (f"{accountPath}/First.txt", "w+") as f: #make First.txt
                f.write(str(self.firstName))
            with open (f"{accountPath}/Last.txt", "w+") as f: #make Last.txt
                f.write(str(self.lastName))
            with open (f"{accountPath}/Hint.txt", "w+") as f: #make Hint.txt
                f.write(str(self.hint))
                
            #TODO: Add a way to create DataStorage/{self.username}/Accounts
            return True