try:
    No=float(input("enter a number to check whether it is an even or odd"))
    def CalC(a):
        if (a%2)==0:
            print("entered number is an even number")
        else:
        	print("entered number is an odd number")
    CalC(No)
except:
	print("not valid")