
Total=0
Count=0
Average=1
class ClassWXY:
 def __init__(self,total,count,average):  
  self.total=total
  self.count=count
  self.average=average
 def CalC(self):
  while True:
   self.a=input("Enter a Number")
   if (self.a).isalpha()==True:
    if "done" in (self.a):
     break
    else:
     continue
   else:
    self.b=int(self.a)
    self.total=(self.total)+(self.b)
    self.count=(self.count)+1
    continue
  self.average=(self.total)/(self.count)
  print("total is {0},total count is {1} and Average is {2}".format(self.total,self.count,self.average))
ClassWXY(Total,Count,Average).CalC()













