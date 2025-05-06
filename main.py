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
login=Login.Run()

print("User: Test")
print("Password: Password123!@")
#Login should output (True or False)
#If

#Login[1] is the account username
if login.Login()[0]:
    match input("Would you like to add(1),delete(2),or modify(3) an account? or exit (0)"):
        case 0:
            exit()
        case 1:
            print("Creating account...")
            register = Register.Registration(True).makePassword(input("Enter password for new account: "))
        case 2:
            print("Deleting account...")
        case 3:
            print("Modifying account...")

        #TODO: Add a way to add/delete accounts and categories and modify account info, 
        #if modifying password reuse register password make function :)
else:
    exit() 