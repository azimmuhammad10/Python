# try:
#  class CalC:
#   #def __init(self):
#   def CalCC(self,a):
#    self.z=a
#    self.a=self.z.lower()
#    print(self.a)

#  A=CalC()
#  A.CalCC(B)

# except:
#  print("Check the script again")
 
a='Ramesh is 18 year rameshwaram . raMeSh works in ISRO . I think ramesH stays in Bangalore '
print(a)
b=a.title()
print(b)
c=input("Enter the word which has to be changed")
h=len(c)
z=list(())
d=len(b)
covered=0
while covered<len(b):
 e=b.find(c,covered)
 if e is not -1:
  z.append(e)
 covered=(e+h)-1
print(z)
