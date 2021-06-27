#Program to print the total no.of vowels in a specific file
def CalC(c):
 count=0
 b="a" or"e" or"i" or"o" or"u" or "A" or "E" or "I" or "O" or "U"
 for x in c:
  if x==b:
   count=count+1
 print(count) 
A=open("mbox.txt","r")
B=(A.read())
print(len(B))
CalC(B)