try:
 A=open("empty2.txt","a")
 A.write("New file has been created")
 A.close()
 B=open("empty2.txt","r")
 print(B.read())
 B.close()
except:
 print("check the script again")