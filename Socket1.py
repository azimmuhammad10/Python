import socket
aa=""
s = socket.socket()
port = 80
s.bind(('', port))
s.listen(5)
while True:
 c, addr = s.accept()
 print ("Socket Up and running with a connection from",addr)
 rcvdData = c.recv(1024).decode()
 if rcvdData=="OK" :
  a=open("data.txt","r")
  for x in a:
   
   aa=aa+"\n"+x
  a.close()
  kk="hi Boss"
  c.send(aa.encode());
  c.close()
  s.close()