'''
Method to take in user input to store Account(username, password) based on categories.
Accounts must be able to be pulled based on categories.
Each account needs the following data:
User Folder Name = ({Id}:{UserName})
Hint.txt
Name.txt

Password folder
ID.txt
Password.txt as sha256

Utilize a text file as a database(each thing has a folder in the user folder
)



Category.csv (User created, If multiple on one user seperate by line)


create a class to check this



'''
import Modules.Login as Login
import Modules.Register as Register
import os

login=Login.Run()
global Username
Loggedin,Username = login.Login()
exit = False
#Login should output (True or False)
#If

def listCategories(Username,Master):
                folders = []
                path = f"Modules/DataStorage/{Username}/Accounts"
                if login.Check(Master,Username):
                    for name in os.listdir(path): #Used the os docs to find some things here, i knew about the library
                        if os.path.isdir(os.path.join(path, name)):
                            folders.append(name)
                    print(f"\nCategories\n\t{folders}")
                else:
                    print("\nIncorrect password...")
                    return

def listAccounts(Username,Master,Category):
                if Category == None:
                    Category=input("\nEnter the Category: ")
                folders = []
                path = f"Modules/DataStorage/{Username}/Accounts/{Category}"
                if login.Check(Master,Username):
                    for name in os.listdir(path): #Used the os docs to find some things here, i knew about the library
                        if os.path.isdir(os.path.join(path, name)):
                            folders.append(name)
                    print(f"\nAccounts\n\t{folders}")
                else:
                    print("\nIncorrect password...")
                    return
def askForMaster():
    Master = input("\nEnter your master password: ")
    if not(Login.Run.Check(Login.Run(),password=Master,username=Username)):
        return (False,None)
    return (True,Master)
#Login[1] is the account username

if Loggedin:
    while not exit:
        match int(input('''
Would you like to...
add an account (1)
delete an account (1)
modify an account (2) 
list Categories (3)
list accounts in a category (4)
show account password (5)
or exit (0)
    ''')):
            case 0:
                exit = True
                break
            case 1: #Add or delete account
                register=Register.Registration(True)
            case 2: # Modify account
                valid,Master = askForMaster()
                if valid:
                    listCategories(Username,Master)
                    Category = input("\nWhat catagory is the account in: ")
                    listAccounts(Username,Master,Category=Category)
                    Account = input("\nEnter the account name: ")
                    with open(f"Modules/DataStorage/{Username}/Accounts/{Category}/{Account}/Password.txt", "r+") as f:
                        f.truncate(0)
                        nPass=input("Enter New Password: ")
                        register = Register.Registration.verify(Register,nPass)
                        f.write(nPass)
            case 3: #List categories
                valid,Master = askForMaster()
                if valid:
                    listCategories(Username,Master)
                    Master = None
            case 4: #List accounts in a category
                valid,Master = askForMaster()
                if valid:
                    listCategories(Username,Master)
                    listAccounts(Username,Master,None)
                    Master = None
            case 5: #Show account details
                valid,Master = askForMaster()
                if valid:
                    listCategories(Username,Master)
                    Category = input("\nEnter the Category: ")
                    listAccounts(Username,Master,Category=Category)
                    Account = input("\nEnter the account name: ")
                    path = f"Modules/DataStorage/{Username}/Accounts/{Category}/{Account}"
                    if login.Check(Master,Username):
                        with open(f"{path}/Password.txt","r") as f:
                            Password = f.readline().strip()
                        print(f"\n{Account}\n\tPassword: {Password}")
                    else:
                        print("\nIncorrect password...")
                    Master = None
else:
    exit = True