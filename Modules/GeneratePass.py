import random as rand

class Generate:
    def __init__(self):
        print("Generating...")
    def Gen(self):
        passw=[]
        cap=False
        spec=False
        num=False
        # return "Password123!"
        while len(passw) <= 8:
            if len(passw) >=5:
                if spec==False:
                    passw.append(chr(rand.randint(35,38)))
                if cap==False:
                    passw.append(chr(rand.randint(65,90)))
                if num==False:
                    passw.append(str(rand.randint(0,9)))
            selector=rand.randint(1,4)
            if selector==1:
                passw.append(str(rand.randint(0,9)))
                num=True
            elif selector==2:
                passw.append(chr(rand.randint(65,90)))
                cap=True
            elif selector==3:
                passw.append(chr(rand.randint(97,122)))
            elif selector==4:
                passw.append(chr(rand.randint(35,38)))
                spec=True
        return "".join(passw)
                
                    
    #DONE!