#To check no.of mails received by each email id's
def CalC():
 b=dict(())
 a=open("mbox-short.txt","r")
 for x in a:
  if "From" in x:
   c=x.split()
   if c[1] not in b.keys():
    b.update({c[1]:1})
   else:
    d=c[1]
    e=b.get(d)
    e=e+1
    b[d]=e
 print(b)   
CalC()