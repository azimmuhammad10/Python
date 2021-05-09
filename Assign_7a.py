try:
 NHours=input("enter no.of hours")
 NHours1=float(NHours)
 HRate=input("enter hourly rate")
 HRate1=float(HRate)
 def CalC(a,b):
   if a <= 40 :
  	  TotAmount=a*b
  	  print(TotAmount)
           
   else :
       TotAmount=(40*b)+((a-40)*3*b)
       print(TotAmount)        
 CalC(NHours1,HRate1)
except:
	print("not valid")



