import Modules.Register
# Log in to run the program:
# Include a hint.
# Limit the number of login attempts to 3 before the program shuts down.
# If the user is a first-time user, Run Register module.

class Run:
    def __init__(self):
        pass
    def start(self, password):
        if password == "Test":
            return True,"id"
        else:
            return False