try:
 Fact=int(input("Enter a number to find its factorial"))
 def CalC(a):
  if a<0:
   print("Entered number cannot be taken as an input since the number is below 0")
  else:
   result=1
   for x in range(1,(a+1)):
    result=result*x
   print(result)
 CalC(Fact)
except:
 print("Not Valid")
     