try:
    KM=float(input("enter distance kilometre"))
    def CalC(a):
        Mile=(a*0.6214)
        print("Distance in miles is {0}".format(Mile))
    CalC(KM)
except:
    print("not valid")