
a = "this is string example....wow!!!   "
print  a.capitalize()
###
##
##
str1 = "chetan"
print  str1.center(200, '@')


##
##
##
##
str = " Rahul "
print str.center(100,' ')
##
##
##
##
##
str = "this is  this is string example....wow is a great person        is!!!"
sub = "is"
hel = 'this is'
print "str.count('this is',0,40) : ", str.count(hel,0,40)

sub = "is"
print "str.count(sub) : ", str.count(sub)
##
##
##
##
##
##
####
####
Str = "this is string example....wow!!!"
Str2 = Str.encode('base64','strict')

print Str2
Str = "this is string example....wow!!!"
Str2 = Str.encode('base64','strict')
print Str2
Str = "this is string example....tow!!!"
Str2 = Str.encode('base64','strict')


print Str
print Str2

##print "Encoded String: " + Str
print "Decoded String: " + Str2.decode('base64','strict')
####
####
##
##
##
##
##
##
a=['sdasa','asasa sharma','asasas','sdadsdsd sharma']
str = "this is string example....wow!!!"

suffix = " example....wow!!!"
print str.endswith(suffix)

##
##suffix = "is"
##print str.endswith(suffix, 2, 4)
##
##
##

str = "this is\tstring example....wow!!!"


print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(50)





str1 = "this is string examplwowe....wow!!!  hi wow"
str2 = "string"

print str1.find(str2,27,40)

print str1.find(str2)


print 'index'


str1 = "this is string example.... is wow!!!"
str2 = "is"

print str1.index(str2)
print str1.index(str2)
print str1.find(str2)
print str1.find(str2)



str = "this2009"
print str.isalnum()

str = "this is string example....wow!!!"
print str.isalnum()


print 'isalpha'


str = "this55"
print str.isalpha()

str = "this"
print str.isalpha()


print 'isdigit'


str = "123456"  # Only digit in this string
print str.isdigit()

str = "this is string example....wow!!!"
print str.isdigit()




print 'is lower '


str = "THIS is string example....wow!!!"
print str.islower()

str = "this is string example....wow!!!"
print str.islower()


print 'isnumeric'

str = u"this2009";  
print str.isnumeric()

str = u"23443434";
print str.isnumeric()

print 'istitle'

str = "This Is String Example...Wow!!!"
print str.istitle()

str = "This is string example....wow!!!"
print str.istitle()


print 'isupper'


str = "THIS IS STRING EXAMPLE....WOW!!!"
print str.isupper()

str = "THIS is string example....wow!!!"
print str.isupper()

print 'join'

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )


print 'lower'


str = "t";

print "Length of the string: ", len(str)

str = "THIS IS STRING EXAMPLE....WOW!!!";

print str.lower()


print 'lsstrip'


str = "88888this is string 8 example....wow!!!";
print str.lstrip()
print str.lstrip('8')

print 'translate'
##
##intab = "aeiou"
##outtab = "12345"
##trantab = maketrans(intab, outtab)
##
##str = "this is string example....wow!!!"
##print str.translate(trantab)


print 'max min'


str = "this is really a string example....wow!!!";
print "Max character: " + max(str)

str = "this is a string example....wow!!!";
print "Max character: " + max(str)


str = "this-is-real-string-example....wow!!!";
print "Min character: " + min(str)

str = "this-is-a-string-example....wow!!!";
print "Min character: " + min(str)


str = "this-is-real-string-example....wow!!!";
print "Min character: " + min(str)

str = "this-is-a-string-example....wow!!!";
print "Min character: " + min(str)


str1 = "this is really a string example....wowis!!!";
str2 = "is";

print str1.rfind(str2)

print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)

print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 0)


str1 = "this is string is example....wow!!!";
str2 = "is";

print str1.rindex(str2)
print str1.index(str2)

print ' rjustttttttttttttttttttttttttttttttttttttttttttttttttttt'
str = "this is string example....wow!!!";

print str.rjust(100, '0')


str = "     this is string example....wow!!!     ";
print str.rstrip()
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8')



str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split('-' )
print str.split(' ', 1 )



str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str.splitlines( )
print str.splitlines( 0 )
print str.splitlines( 3 )
print str.splitlines( 4 )
print str.splitlines( 5 )


str = "this is string example....wow!!!";
print str.startswith( 'this' )
print str.startswith( 'is', 2, 4 )
print str.startswith( 'this', 2, 4 )


str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' )


str = "this is string example....wow!!!";
print str.swapcase()

str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.swapcase()

str = "this is string example....wow!!!";
print str.title()

##
##intab = "aeiou"
##outtab = "12345"
##trantab = maketrans(intab, outtab)
##
##str = "this is string example....wow!!!";
##print str.translate(trantab)


str = "this is string example....wow!!!";

print "str.capitalize() : ", str.upper()


str = "this is string example....wow!!!";

print str.zfill(40)
print str.zfill(50)


str = "this is string example....wow!!!";

print str.zfill(40)
print str.zfill(50)