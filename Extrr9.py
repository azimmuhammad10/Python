#sorting the values in dict
def CalC(A): #function 
 AA=dict(())#empty dict
 B=list(A.values())#list having values
 B.sort() #sorting the values
 for a in B:#loops through list 
  for b,c in A.items():#loops through dict
   if a==c:#compares list value with dict
    AA[b]=c#if condition is true- adds key as well as value to empty dict
 print(AA)#print new dict

A={"a":98,"b":99,"c":108,"d":54,"e":68,"f":45,"g":9}#dictionary keys and values before
print("Before")
print(A)#print the above statement  
print("after")
CalC(A)#function call


