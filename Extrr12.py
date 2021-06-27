def CalC():
 a=input("Enter the file name")
 b=open(a,"r")
 tot=0
 lines=0
 for c in b:
  if c.startswith("X-DSPAM-Confidence:"):
   lines=lines+1
   d=float(c[19:])
   tot=tot+d
 print("Total=",tot)
 print("Total Lines=",lines)
 e=tot/lines
 print("Average=",e)
CalC()

