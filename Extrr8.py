#program to input numbers to a list and finding sum of it
def CalC(a):
 sum=0
 for x in a:
  sum=sum+x
 print(sum)
 print(a)
A=list()
while True:
 B=input("enter numbers")
 if B =="done":
  break
 else:
  C=int(B)
  A.append(C)
CalC(A)
  

