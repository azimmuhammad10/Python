#To check which day of the week has received more no.of email's
def CalC():
 b=dict(())
 a=open("mbox-short.txt","r")
 for x in a:
  if "From" in x:
   c=x.split()
   if len(c)>=3:
    if c[2] not in b.keys():
     b.update({c[2]:1})
    else:
     d=c[2]
     e=b.get(d)
     e=e+1
     b[d]=e
 print(b)   
CalC()