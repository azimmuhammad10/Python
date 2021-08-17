try:
 class CalC:
  #def __init(self):
  def CharChk(self,a):
   self.z=a
   count=0
   for x in self.z:
    if x.isalpha():
     count=count+1
   return count
  
  def NoChk(self,a):
   self.z=a
   count=0
   for x in self.z:
    if x.isdigit():
     count=count+1
   return count
 
  def SpecialChk(self,a):
   self.z=a
   count=0
   self.b=["!","@","#","%","^","&","*"]
   for x in self.z:
    if x.isspace() is False:
     for y in self.b:
      if x==y:
       count=count+1
   return count
    
  def CalCC(self):
   self.a=input("Enter Password")
   if len(self.a)<8:
    print("Password length shouldn't be less than 8 ")
   self.b=CalC().CharChk(self.a)
   if self.b <2:
    print("Password should contain atleast 2 Alphabets")
   self.c=CalC().NoChk(self.a)
   if self.c < 2:
    print("Password should contain atleast 2 numbers")
   self.d=CalC().SpecialChk(self.a)
   if self.d <2:
    print("Password should contain atleast 2 Special Characters")
 A=CalC()
 A.CalCC()

except:
 print("Check the script again")