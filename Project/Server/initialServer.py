import socket
import re
class CalC:
 
 def SocketSocket(self):
  a=""
  s = socket.socket()
  port = 987
  s.bind(('', port))
  s.listen(5)
  while True :
   c, addr = s.accept()
   print ("Received request from:",addr)
   b= c.recv(1024).decode()
   if b=="send" :
    d=open("data.txt","r")
    for x in d:
     x.strip()
     a=a+x 
    d.close()
    c.send(a.encode());
    a=""
    c.close()
   elif re.search('^receivepass:.*',b):
    bbbb=b[12:]
    k=open("data.txt","a")
    l="\nxpxp:{0}".format(bbbb)
    k.write(l)
    k.close()
    c.close()
   else :
    g=open("data.txt","a")
    h="\nxuxu:{0}".format(b)
    g.write(h)
    g.close()
    c.close()
    break
  while True:
   aa,addr3=s.accept()
   print("Received request from:",addr3) 
   bb=aa.recv(1024).decode()
   cc=open(bb,"a")
   for x in cc:
    print(x)
   cc.close()
   aa.close()


A=CalC()
A.SocketSocket()