try:
    A=int(input("enter a"))
    B=int(input("enter b"))
    def CalC(a,b):
        c=a
        a=b
        b=c
        print("a={0} , b={1}".format(a,b))
    CalC(A,B)
except:
    print("not valid")
