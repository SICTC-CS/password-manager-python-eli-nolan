from Modules.Register import Registration

# Log in to run the program:
# After 1 failed attempt show hint for userName
# Limit the number of login attempts to 3 before the program shuts down.
# If the user is a first-time user, Run Register module. 
class Run:
    def __init__(self):
        print("Ran login, Running registration")
        reg = Registration(False)
        if reg:
            print("Registerd")
