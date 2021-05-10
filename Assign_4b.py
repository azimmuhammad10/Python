try:
    Mile=float(input("enter distance in miles"))
    def CalC(a):
        KM=(a/0.6214)
        print("Distance in kilometre is {0}".format(KM))
    CalC(Mile)
except:
    print("not valid")