
from init 
init()
from ansi import Fore,Back,Style
print(Fore.RED+"some red text")
class CalC:#Main Class
  #def __init__(self):

 """ data.txt , converts to lower, recursion ,lstrips each line , startswith condition --1
 """
 def CredentialsCheck(self,inp):
  try:
   self.a=open("data.txt","r")
   self.b=inp
   self.b=self.b.lower()
   for x in self.a :
    g=x.strip()
    if g.startswith("xuxu:"):
     h=g[5:]
     if self.b == h:
      self.a.close()
      print("Username already exists")
      c=input("Username:")
      d=CalC().CredentialsCheck(c)
      return d
   self.a.close()
   return inp
  except:
   print("database missing")
 
 #username to data--2
 def SendUser(self,inp):
  self.a=inp
  self.b=open("data.txt","a")
  self.c="\n xuxu:{0} \n".format(self.a)
  self.b.write(self.c)
  self.b.close()

#Pass to data--3
 def SendPass(self,inp):
  self.a=inp.lower()
  self.b=open("data.txt","a")
  self.c="\n xpxp:{0} \n".format(self.a)
  self.b.write(self.c)
  self.b.close()


 """
  a=Username, b=Password ,CredentialsCheck --4--1,2,3

 """
 def Create(self):
  self.a=input("Username:") 
  a=CalC().CredentialsCheck(self.a)
  CalC().SendUser(a)
  self.b=input("Password:")
  CalC().SendPass(self.b)
  print("Account Created Successfully")
  CalC().LoginMain()
  """---------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------------------------------------------------------------------------
  """
 #Matches pass --5
 def LoginPass(self,inp):
  self.countt=0
  self.a=inp+2
  self.b=open("data.txt","r")
  for x in self.b:
   self.countt=self.countt+1
   if self.countt==self.a:
    b=x.strip()
    c=b[5:]
    break
  return c



 #Searches username in data --6---5
 def SearchData(self,inp):
  value=0
  countt=0
  o=""
  self.a=open("data.txt","r")
  self.b=inp
  self.b=self.b.lower()
  for x in self.a :
   countt=countt+1
   g=x.strip()
   if g.startswith("xuxu:"):
    h=g[5:]
    if self.b == h:
     value=1
     self.a.close()
     o=CalC().LoginPass(countt)
     break
 
  return value,o
 
 
 # Loginmain --7---6
 def LoginMain(self):
  print("Please enter login credentials")
  a=input("Username:")
  b,o=CalC().SearchData(a)
  while b!=1:
   print("Username not found ")
   c=input("Username")
   b,o=CalC().SearchData(c)
  print(o)
  



 # def HeadBanner(self):

 #Initial command checker--8--4,7
 def CommandCheck(self,a):
  self.a=a
  if self.a == "c" or self.a =="C" :
   CalC().Create()
  elif self.a =="j" or self.a =="J" :
   CalC().LoginMain()

#Calls
A=CalC()
print("C or c - To Create Account --- J or j - Login")
B=input("Enter Command")
A.CommandCheck(B)

   


