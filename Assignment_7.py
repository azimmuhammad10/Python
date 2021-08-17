try:
 class CalC:
  #def __init(self):
  def CalCC(self,a,b):
   self.e=list(())
   self.c=a.sort(reverse=True)
   self.g=0
   for x in self.c:
    for y in a:
     if x==y:
      self.d=a.index(y)
      self.f=b[d]
      self.e.insert(self.g,self.f)
    self.g=self.g+1
   print("Sorted Marks List:",self.c)
   print("Respective names:",self.e)

 B=['candy','brain','damu','sujoy']
 C=[90,95,60,79]
 A=CalC()
 A.CalCC(C,B)

except:
 print("Check the script again")