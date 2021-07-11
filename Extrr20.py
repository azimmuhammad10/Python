import re
class CalC:
 def CalCC(self):
  self.a=open("mbox.txt","r")
  for x in self.a:
   self.b=re.findall("http:.*",x)
   print(self.b)

CalC().CalCC()
