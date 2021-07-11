#Program to extract the word written inside parenthesis from a string
import re
class CalC:
 def CalCC(self):
  self.a=open("mbox.txt","r")
  for x in self.a:
   self.b=re.findall("[(].*[)$]",x)
   print(self.b)

CalC().CalCC()

