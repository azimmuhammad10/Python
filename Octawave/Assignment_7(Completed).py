try:
 class CalC:
  #def __init(self):
  def CalCC(self,a,b):
   self.a=a
   self.b=b
   self.d=list(())#--self.d->Initial list values
   self.f=list(())
   for x in self.a:
   	self.d.append(x)
   self.a.sort(reverse=True)
   for y in self.a :
   	self.e=self.d.index(y)
   	self.g=self.b[self.e]
   	self.f.append(self.g)#--self.f->Updated Names
   print("Initial Marks:",self.d)
   print("Respective Names:",self.b)
   print("Sorted Marks:",self.a)
   print("Respective Names:",self.f)

 B=['candy','brain','damu','sujoy']
 C=[90,95,60,79]
 A=CalC()
 A.CalCC(C,B)

except:
 print("Check the script again")