try:
 Total=0
 Count=0
 Average=1
 Smallest=None
 Largest=None
 Arr=[]
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
   for x in Arr:
    Arr.append(x)
    if x> Largest:
      Largest=x
    elif x< Smallest:
      Smallest=x
    else:
      break
   break 
   continue
 average=total/count
 print("total is {0} , count is {1} and average is {2}".format(total,count,average))
except:
 print("check the script again")

