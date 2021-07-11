#Program to arrange the numbers in ascending order using RE from a file 
import re
class CalC:

 def CalCC(self):
  a=open("mbox-short.txt","r")
  for x in a:
   b=re.findall("\d",x)
   b.sort()
   print(b)
  a.close()

CalC().CalCC()