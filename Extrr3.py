try:
 A=open("empty.txt","r")
 print("Before")
 print(A.read())
 A.close()
 B=open("empty.txt","a")
 B.write(" New line has been added")
 B.close()
 D=open("empty.txt","r")
 print("After")
 print(D.read()) 
 D.close()
except:
 print("check the script again")
