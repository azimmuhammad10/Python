try:
 No=int(input("Enter a number to display its multiplication table"))
 def CalC(a):
  for x in range(1,(11)):
   print("{2} x {0} ={1}".format(x,(a*x),a))
 CalC(No)
except:
 print("Not Valid")