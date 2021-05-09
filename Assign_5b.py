try:
	Fah=input("enter temperature in Fahrenheit")
	Fah1=float(Fah)
	def Calc(a):
		Cel=((a-32)*(5/9))
		print(Cel)
	Calc(Fah1)
except:
	print("not valid")
	