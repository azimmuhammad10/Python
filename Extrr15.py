#program to find if the specified word matches with the last word of the string
import re 
a="hoping all are fine"
b= re.findall("fine$",a)
if b:
  print("Match found")
else:
  print("Match not found")
