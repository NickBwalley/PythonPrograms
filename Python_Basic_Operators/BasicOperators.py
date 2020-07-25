'''
Operator    	    Name
+	Addition    	x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''

'''PYTHON ARITHMETIC OPERATORS'''
# a and b are operands
a = 10
b = 20

print(a+b) # Addition
print(a-b) # Subtraction
print(a/b) # Division
print(a*b) # Multiplication
print(b%a) # modulus
print(b**a) # Exponent (b=20 to the power a=10)
a = 9
b = 2
print(a//b) # Floor Division
print("--------------------------------------------")
''' PYTHON COMPARISON OPERATOR'''
a = 49
b = 99
# returns boolean
print(a==b) # False
print(a!=b) # True
# print(a<>b) # same as the != operator
print(a>b) # False
print(a<b) # true
print(a>=b) # False
print(a<=b) # True
print("--------------------------------------------")
'''PYTHON ASSIGNMENT OPERATORS'''
a = 40
b = 60

c = a+b # assigns c to the operation a+b
print(c)
c += a # The same as c = c+a
print(c)
c -= a # The same as c = c+a
print(c)
c *= a # The same as c = c*a
print(c)
c /= a # The same as c = c/a
print(c)
###########
print("--------------------------------------------")
a = 5
b = 20
b %=a # The same as b = b%a
print(b)
a **=a # Means a = a**
print(a)
a //=a # performs a floor division and returns the value to the left operand
print(a)
print("--------------------------------------------")

''' PYTHON MEMBERSHIP OPERATOR'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")
if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")
a = 2
if ( a in list ):
    print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")
print("--------------------------------------------")

''' PYTHON IDENTITY OPERATOR'''
a = 20
b = 20
if ( a is b ):
    print ("Line 1 - a and b have same identity")
else:
    print ("Line 1 - a and b do not have same identity")
if ( id(a) == id(b) ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")
b = 30
if ( a is b ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")
if ( a is not b ):
    print ("Line 4 - a and b do not have same identity")
else:
    print ("Line 4 - a and b have same identity")