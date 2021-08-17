try:
 class CalC:
  #def __init(self):
  def CalCC(self):
   self.a='Robin age 45 salary 1 Lakh . Rahul age 46 salary 2 Lakh . Ramya age 39 salary 1.5 Lakh'
   self.b=self.a.split()
   self.c=input("Enter the Name")
   self.d=self.b.index(self.c)
   self.age=self.b[(self.d)+2]
   self.salary=self.b[(self.d)+4]
   print(self.c,self.age,self.salary)
 CalC().CalCC()
except:
 print("check the script again")