from colorama import init 
init()
from colorama import Fore,Back,Style
import re
import socket

class CalC:#Main Class
  #def __init__(self):

 """ data.txt , converts to lower, recursion ,lstrips each line , startswith condition --1
 """
 def Sock(self):
  s = socket.socket()
  s.connect(('127.0.0.1',80))
  a="send"
  s.send(a.encode());
  g=s.recv(1024).decode()
  s.close()
  return g

 def SockAppend(self,a):
  s = socket.socket()
  s.connect(('127.0.0.1',80))
  sa=a
  s.send(sa.encode())
  s.close()

 def SockAppendPass(self,a):
  s = socket.socket()
  s.connect(('127.0.0.1',80))
  sa="receivepass"+":"+a
  s.send(sa.encode())
  s.close()

 def CredentialsCheck(self,inp):
  a=CalC().Sock()
  self.b=inp
  self.b=self.b.lower()
  b=a.split("\n")
  for x in b:
    if re.search('^xuxu:.*',x):
      c=x[5:]
      if self.b == c:
       print(Back.WHITE+Fore.RED+Style.DIM+"----||Username already exists||----")
       print(Back.RED+Fore.WHITE)
       c=input("Username:")
       d=CalC().CredentialsCheck(c)
       return d
  print(Style.RESET_ALL)
  return inp
 
 #username to data--2
 def SendUser(self,inp):
  self.a=inp
  CalC().SockAppend(self.a)

#Pass to data--3
 def SendPass(self,inp):
  self.a=inp.lower()
  CalC().SockAppendPass(self.a)


 """
  a=Username, b=Password ,CredentialsCheck --4--1,2,3

 """
 def Create(self):
  print(Back.RED+Fore.WHITE)
  self.a=input("Username:") 
  self.b=CalC().CredentialsCheck(self.a)
  CalC().SendUser(self.b)
  print(Back.RED+Fore.WHITE)
  self.c=input("Password:")
  CalC().SendPass(self.c)
  print(Back.WHITE+Fore.RED+Style.DIM+"----||Account Created Successfully||----")
  d,e=CalC().LoginMain()
  print(Style.RESET_ALL)
  return d,e
  """---------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------------------------------------------------------------------------
  """
 #Matches pass --5
 def LoginPass(self,inp,oo):
  value=0
  s_o_c_k=CalC().Sock()
  b=s_o_c_k.split("\n")
  oo_1=oo
  d=b[oo_1]
  e=d[5:]
  if e==inp:
   value=1

  return value,inp
 #Searches username in data --6---5
 def SearchData(self,inp):
  s_o_c_k=CalC().Sock()
  value=0
  countt=0
  o=""
  self.b=inp
  self.b=self.b.lower()
  b=s_o_c_k.split("\n")
  for x in b:
    countt=countt+1
    if re.search('^xuxu:.*',x):
     c=x[5:]
     if self.b == c:
      value=1
      break
 
  return value,countt,self.b
 
 
 # Loginmain --7---6
 def LoginMain(self):
  print(Back.WHITE+Fore.RED+Style.DIM+"----||Please enter login credentials||----")
  print(Back.RED+Fore.WHITE)
  a=input("Username:")
  b,o,usern=CalC().SearchData(a)
  while b!=1:
   print(Back.WHITE+Fore.RED+Style.DIM+"----||Username not found||---- ")
   print(Back.RED+Fore.WHITE)
   c=input("Username:")
   b,o,usern=CalC().SearchData(c)
  print(Back.RED+Fore.WHITE)
  d=input("Password:")
  bb,userp=CalC().LoginPass(d,o)
  while bb!=1:
   print(Back.WHITE+Fore.RED+Style.DIM+"----||Incorrect Password||----")
   print(Back.RED+Fore.WHITE)
   bb3=input("Password")
   bb,userp=CalC().LoginPass(bb3,o)
  #print("Login Successfull")
  print(Style.RESET_ALL)
  return usern,userp
  




 # def HeadBanner(self):

 #Initial command checker--8--4,7
 def CommandCheck(self,a):
  self.a=a
  if self.a == "c" or self.a =="C" :
   b,c=CalC().Create()
  elif self.a =="j" or self.a =="J" :
   b,c=CalC().LoginMain()
  return b,c

 def Dashboard(self,a):
  self.a=a
  self.c=""
  while self.c!="exit":
    print(Back.WHITE+Fore.RED+Style.BRIGHT+"----||Logged in as {0}||----".format(a))
    print(Back.WHITE+Fore.RED+Style.DIM+"----||inbox - Check inbox --- compose - Compose message||----")
    print(Back.WHITE+Fore.RED+Style.DIM+"----||switch - Switch Account --- exit - Exit||----")
    print(Back.RED+Fore.WHITE)
    self.c=input("Enter Command")
  
   
   # break

#Calls
A=CalC()
print(Back.WHITE+Fore.RED+Style.DIM+"----||C or c - To Create Account --- J or j - Login||----")
print(Back.RED+Fore.WHITE)
B=input("Enter Command")
print(Style.RESET_ALL)
C,D=A.CommandCheck(B)#Password received
A.Dashboard(C)
   


