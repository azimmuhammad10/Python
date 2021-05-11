try:
 No=int(input("enter a number to check whether it is a prime number or not"))
 def CalC(a):
  b=0
  if a>1:
   for x in range(2,a):
    if (a%x)==0:
     b=0
     break
    else:
     b=1 
  else:
   print("Entered number is not a prime number") 
  if b==1:
   print("Entered number is a prime number")
  else:
   print("Entered number is not a prime number")
 CalC(No)  
except:
 print("not valid")     
