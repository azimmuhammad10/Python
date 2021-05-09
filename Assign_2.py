try:
    print("enter a,b,c below to find roots of quadratic equation")
    A=float(input("enter a"))
    B=float(input("enter b"))
    C=float(input("enter c"))
    def CalC(a,b,c):
        q=((b*b)-(4*a*c))	   
        if q < 0:
            print("roots are complex numbers")
            print("root 1= {0}".format(((-b)/(2*a))+((-q**0.5)/(2*a))))
            print("root 2= {0}".format(((-b)/(2*a))-((-q**0.5)/(2*a))))
        elif q == 0:
	        print("roots are equal")	
	        print("roots = {0}".format((-b)/(2*a)))
        else:
	        print("roots are real numbers")
	        print("root 1= {0}".format(((-b)/(2*a))+((q**0.5)/(2*a))))
	        print("root 2= {0}".format(((-b)/(2*a))-((q**0.5)/(2*a))))
    CalC(A,B,C)
except:
    print("not valid")    
	

