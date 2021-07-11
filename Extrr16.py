import re 
a=open("mbox-short.txt","r")
for x in a:
 b=re.search("^From.",x)
 print(b)