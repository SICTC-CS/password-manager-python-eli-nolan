import Modules.CheckPassReq
import Modules.GeneratePass
import hashlib
import os
from shutil import rmtree 

class Registration():
    def __init__(self,LoggedIn):
        self.LoggedIn = LoggedIn
        #Get username
        self.userName = input("Enter your username: ")
        if LoggedIn:
            self.account = input("Enter the account name: ")
            self.category = input("Enter the category you want to put this in: ")
        #Get password
        print("\nPassword must contain:\n\tAtleast 1 special character\n\tAtleast 1 number\n\tAtleast 8 characters\n")
        self.password = input("Enter a password Or enter 'n' to generate a master password: ")
        self.makePassword(self.password,LoggedIn)
        # print(f"Initial password: {self.password}")#for DEBUG
        #Get name
        if not LoggedIn:
            self.firstName = input("Enter your first name: ")
            self.lastName = input("Enter your last name: ")
            if self.lastName != None:
                self.store()
        else:
            if self.hint != None:
                self.store()
    def makePassword(self,InitialPassword,LoggedIn): # Verifys and encrypts the password allowing the user to make a password
        if InitialPassword.lower() != "n":
            password = InitialPassword
            #Verification of password and allowing reinput
            while not self.verify(password)[0]:
                print(self.verify(password)[1])
                if not LoggedIn:
                    password = input("Enter a new Master password: ")
                else:
                    password = input("Enter a new password: ")
                
            #Password encryption 
            if self.verify(password)[0]:
                if not LoggedIn:
                    self.password = self.encrypt(password)
                else:
                    self.password = password
                # print(f"Encrypted password: {self.password}") #for DEBUG
            #Create hint
            if LoggedIn == False:
                self.hint = input("Enter a hint for if you forget your master password: ")
                print(f"Hint: '{self.hint}'")
            else:
                self.hint=""
        else:
            Generator = Modules.GeneratePass.Generate()
            password = Generator.Gen()
            if not LoggedIn:
                self.password = self.encrypt(password)
            else:
                self.password = password
            print(f"Generated master password: {password}")
            # print(f"DEBUG Encrypted password: {self.password}") #for DEBUG

            self.hint = "Randomly generated password..."
            
    def verify(self,password): #Checks password requirements
        requirement = Modules.CheckPassReq.Check()
        return requirement.isValid(password)
    
    def encrypt(self,password): #Encrypts password
        return hashlib.sha256(password.encode('utf-8')).hexdigest() #This encrypts the password using sha 256

    def store(self): #Stores all data
        path = f"Modules/DataStorage"
        if self.LoggedIn:
            accountPath = f"{path}/{self.userName}/accounts/{self.category}/{self.account}"
            action=int(input("Please type 1 to delete, 2 to create account: "))
            if action==1:
                with open(f"{accountPath}/Password.txt", "r") as f:
                    accPass=f.read().strip()
                if self.password==accPass:
                    rmtree(accountPath)
            elif action==2:
                os.makedirs(accountPath,exist_ok=True) #Create the path down to /user 
                
                with open (f"{accountPath}/Password.txt", "w+") as f: #make password.txt
                    f.write(self.password)
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