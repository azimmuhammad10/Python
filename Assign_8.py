try:
    Year=int(input("enter a year to check whether that particular year is a leap year or not"))
    def CalC(a):
        if (a%4)==0:
            if (a%100==0):
                if (a%400)==0:
                    print("Entered year {0} is a leap year".format(a))
                else:
                    print("Entered year {0} is not a leap year".format(a))
            else:
                print("Entered year {0} is a leap year".format(a))
        else:
            print("Entered year {0} is not a leap year".format(a))
    CalC(Year)
except:
    print("Not Valid")        
