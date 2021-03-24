"""
Formatting Types
Inside the placeholders you can add a formatting type to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
"""

# :<		Left aligns the result (within the available space)
# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

# Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))
print()
################

# :>		Right aligns the result (within the available space)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))
print()
#################

# :^		Center aligns the result (within the available space)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))
print()
####################

# :=		Places the sign to the left most position
#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))
print()
####################

# :+		Use a plus sign to indicate if the result is positive or negative
#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))
print()
#######################

# :-		Use a minus sign for negative values only
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))
print()
######################

# : 		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))
print()
#######################

# :,		Use a comma as a thousand separator
#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))
print()
########################

# :_		Use a underscore as a thousand separator
#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))
print()
########################

# :b		Binary format
#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))
print()
########################
# :c		Converts the value into the corresponding unicode character
########################

# :d		Decimal format
#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))
print()
#########################
# :e		Scientific format, with a lower case e
#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))
print()
##########################

# :E		Scientific format, with an upper case E
#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))
print()
###########################
# :f		Fix point number format
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))
print()
##################################

# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))
print()
######################################

# :g		General format
# :G		General format (using a upper case E for scientific notations)
#######################################

# :o		Octal format
#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))
print()
#####################################

# :x		Hex format, lower case
#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))
print()
#######################################

# :X		Hex format, upper case
#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))
print()
##################################
# :n		Number format
############################

# :%		Percentage format
#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))
print()
##########################

