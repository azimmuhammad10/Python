try:
 total=0
 count=0
 average=1
 while True:
  a=input("Enter a Number")
  if a.isalpha()==True:
   if "done" in a:
    break
   else:
    continue
  else:
   b=int(a)
   total=total+b
   count=count+1
   continue
 average=total/count
 print("total is {0} , count is {1} and average is {2}".format(total,count,average))
except:
 print("check the script again")

