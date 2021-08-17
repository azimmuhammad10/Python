aList = []
aList.append('hi')
aList.append('hi')
print ("Updated List : ", aList)

##
##
aList = [123, 'xyz', 'zara', 'abc', 123]

print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))
##
##
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print ("Extended List : ", aList)
##
##
##
##print "Extended List : ", aList
##aList=aList+bList
#print "Extended List : ", aList
##
##aList = [123, 'xyz', 'zara', 'abc',123];
##
##print ("Index for 123 : ", aList.index ( 1236))
##aList[aList.index ( 123)]=0
####print aList
##print "Index for 123 : ", aList.index  (123) 
##print "Index for zara : ", aList.index ( 'zara' )
##
##
aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 1, 20010)
##
print ("Final List : ", aList)
##
##
aList = [123, 'xyz', 'zara', 'abc'];

for i in aList:
    print (i)
##
print ("A List : ", aList.pop())
print ("B List : ", aList.pop())
print ("B List : ", aList.pop())
print ("B List : ", aList.pop())

##
##
##
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');

print ("List : ", aList)
##aList.remove('xyz')
##print "List : ", aList
##aList.remove('abc');
##print "List : ", aList
##
##
##
##
##
aList = [ 'xyz', 'zara','ZAra' ,'Abc', 'Zara','xyz','!','@','#','$','%','^','&']
a = [1,2,3,4,5,6,7,8,9]

aList.sort()
a.sort(reverse=True)

print (aList)
print (a)