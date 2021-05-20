def CalC():
 total=0
 count=0
 avg=0
 while True:
  a=input("Enter a Number")
  b=int(a)
  if a=="done":
   break
  else:
   total=total+b
   count=count+1
  break
 average=total/count
 print("Total is {0} ,total count is {1} and average is {3}".format(total,count,average))
CalC()









