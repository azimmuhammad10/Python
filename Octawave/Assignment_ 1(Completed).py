#Sort 4 numbers in ascending order

try:
 class CalC:
  #def __init(self):
  def CalCC(self):
   self.a=[98,54,34,2]
   self.b=list(())
   self.c=len(self.a)
   while self.c>0:
    self.smallest=self.a[0]
    for x in self.a :
     if x<=self.smallest:
      self.smallest=x
    self.a.remove(self.smallest)
    self.b.append(self.smallest)
    self.c=len(self.a)
   print("After Sorting",self.b)

 A=CalC()
 A.CalCC()

except:
 print("Check the script again")
