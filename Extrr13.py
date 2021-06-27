def CalC():
 try:
  count=0
  a=input("Enter the file name")
  b=open(a,"r")
  for c in b:
   count=count+1
  print(count)
 except:
  print("File Cannot Be Found")
CalC()
