try:
    No=float(input("enter any number to check whether it is positive or negative"))
    def CalC(a):
        if a>0:
            print("number is positive")
        elif a==0:
            print("number is equal to 0")
        else:
            print("number is negative") 
    CalC(No)
except:
    print("not valid")