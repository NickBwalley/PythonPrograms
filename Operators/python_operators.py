"""
Python divides the Operators in the following groups:

Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Identity Operators
Membership Operators
Bitwise Operators

"""

"""PYTHON ARITHMETIC OPERATORS"""
"""
Arithmetic Operators are used with numeric values to perform common mathematical operations:
Operator	Name	        Example	
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	        Multiplication	x * y	
/	        Division	    x / y	
%	        Modulus	        x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y
"""

"""PYTHON ASSIGNMENT OPERATOR"""

"""
Assignment Operators are used to assign values to variables:
Operator	Example	Same As	
=	        x = 5	x = 5	
+=	        x += 3	x = x + 3	
-=	        x -= 3	x = x - 3	
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3	
&=	        x &= 3	x = x & 3	
|=	        x |= 3	x = x | 3	
^=	        x ^= 3	x = x ^ 3	
>>=	        x >>= 3	x = x >> 3	
<<=	        x <<= 3	x = x << 3
"""

"""PYTHON COMPARISON OPERATOR"""

"""
Comparison Operators are used to compare two values:

Operator	Name	        Example	
==	        Equal	        x == y	
!=	        Not equal	    x != y	
>	        Greater than	x > y	
<	        Less than	    x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y
"""

"""PYTHON LOGICAL OPERATORS"""

"""
Logical Operators are used to combine conditional statements:

Operator	Description	Example	
and 	    Returns True if both statements are true	x < 5 and  x < 10	
or	        Returns True if one of the statements is true	x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

"""PYTHON IDENTITY OPERATORS"""

""" 
Identity Operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location:

Operator	Description	Example	
is  	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""

"""
Python Membership Operators

Membership Operators are used to test if a sequence is presented in an object:

Operator	Description	Example	
in 	    Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""
"""
Python Bitwise Operators
Bitwise Operators are used to compare (binary) numbers:

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and
 let the rightmost bits fall off
"""

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
if  a in list :
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
print("--------------------------------------------")

''' PYTHON OPERATORS PRECEDENCE'''
'''
Operator            Description
** Exponentiation   (raise to the power)
~ + - Ccomplement,  unary plus and minus (method names for the last two are +@ and -@)
* / % //            Multiply, divide, modulo and floor division
+ -                 Addition and subtraction
>> <<               Right and left bitwise shift
&                   Bitwise 'AND'
^ |                 Bitwise exclusive `OR' and regular `OR'
<= < > >=           Comparison Operators
<> == !=            Equality Operators
= %= /= //= -= +=
*= **=              Assignment Operators
is, is not          Identity Operators
in, not in          Membership Operators
not or and          Logical Operators

Operator precedence affects how an expression is evaluated.
For example, x = 7 + 3 * 2; here, x is assigned 13, not 20 because operator * has
higher precedence than +, so it first multiplies 3*2 and then adds into 7.
'''
a = 20
b = 10
c = 15
d = 5
e = 0
