try:
 x="Ece students:0.7056"
 print(x)
 print(type(x))
 y=x.find(":")
 z=(x[(y+1):])
 print(z)
 z1=float(z)
 print(type(z1))
except:
 print("error ")
