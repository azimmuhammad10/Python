#Program to replace white space with an underscore
import re
a="a b c d e f g h i j k l m n o p q r s t u v w x y z"
b= re.sub("\s", "_", a)
print(b)
c="a"
