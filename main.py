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
exit = False
print("User: Test")
print("Password: Password123!@")
#Login should output (True or False)
#If

#Login[1] is the account username
if login.Login()[0]:
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
                exit()
            case 1: #Add or delete account
                register=Register.Registration(True)
            case 2: # Modify account
                folders=[]
                Username = input("\nEnter your master username: ")
                path = f"Modules/DataStorage/{Username}/Accounts"
                if login.Check(input("\nEnter your master password: "),Username):
                    for name in os.listdir(path): #Used the os docs to find some things here, i knew about the library
                        if os.path.isdir(os.path.join(path, name)):
                            folders.append(name)
                    print(f"\nCategories\n\t{folders}")
                    catagory=input("What catagory is the account in?")
                    Account=input("What is the account name?")
                    with open(f"{path}/{catagory}/{Account}/Password.txt", "r+") as f:
                        f.truncate(0)
                        nPass=input("Enter New Password: ")
                        Register.Registration.verify(nPass)
                        f.write(nPass)
                else:
                    print("\nIncorrect password...")
            case 3: #List categories
                folders = []
                Username = input("\nEnter your master username: ")
                path = f"Modules/DataStorage/{Username}/Accounts"
                if login.Check(input("\nEnter your master password: "),Username):
                    for name in os.listdir(path): #Used the os docs to find some things here, i knew about the library
                        if os.path.isdir(os.path.join(path, name)):
                            folders.append(name)
                    print(f"\nCategories\n\t{folders}")
                else:
                    print("\nIncorrect password...")
            case 4: #List accounts in a category
                folders = []
                Username = input("\nEnter your master username: ")
                Category = input("\nEnter the Category: ")
                path = f"Modules/DataStorage/{Username}/Accounts/{Category}"
                if login.Check(input("\nEnter your master password: "),Username):
                    for name in os.listdir(path): #Used the os docs to find some things here, i knew about the library
                        if os.path.isdir(os.path.join(path, name)):
                            folders.append(name)
                    print(f"\nAccounts\n\t{folders}")
                else:
                    print("\nIncorrect password...")
            case 5: #Show account details
                Username = input("\nEnter your master username: ")
                Category = input("\nEnter the Category: ")
                Account = input("\nEnter the account name: ")
                path = f"Modules/DataStorage/{Username}/Accounts/{Category}/{Account}"
                if login.Check(input("\nEnter your master password: "),Username):
                    with open(f"{path}/Password.txt","r") as f:
                        Password = f.readline().strip()
                    print(f"\n{Account}\n\tPassword: {Password}")
                else:
                    print("\nIncorrect password...")
            #TODO: Add a way to add/delete accounts and categories and modify account info, 
            #if modifying password reuse register password make function :)
else:
    exit = True