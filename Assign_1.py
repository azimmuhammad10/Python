
try:
	Num=float(input("enter number"))
	def Calc(a):
		Sq=a**0.5
		print("square root of {0} is {1} ".format(a,Sq))
	Calc(Num)
except:
	print("not valid")