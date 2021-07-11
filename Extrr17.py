#Program to find total count,sum,average using RE from a file
import re
class CalC:
 def __init__(self,a,b,c):
  self.sum=a
  self.count=b
  self.average=c

 def CalCC(self):
  a=open("mbox-short.txt","r")
  for x in a:
   b=re.findall("\d",x)
   for x2 in b:
    self.count=self.count+1
    d=int(x2)
    self.sum=self.sum+d
  print("Total count is=",self.count)
  print("Total Sum is=",self.sum)
  print("Average is=",(self.sum)/(self.count))
  a.close()

CalC(0,0,1).CalCC()

