import socket

s = socket.socket()
s.connect(('127.0.0.1',80))
str = input("S: ")
s.send(str.encode());
g=s.recv(1024).decode()
print (g)
s.close()
exit()