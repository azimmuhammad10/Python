try:
	Cel=input("enter temperature in celsius")
	Cel1=float(Cel)
	def CalC(a):
		Fah=((a*(9/5))+32)
		print(Fah)
	CalC(Cel1)
except:
	print("not valid")