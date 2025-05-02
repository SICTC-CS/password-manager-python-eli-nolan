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

import Modules.CheckPassReq as Check
import Modules.Login as Login

login=Login.Run()

print(login.start("Test"))