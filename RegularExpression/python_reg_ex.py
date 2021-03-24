"""# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
#
# Import the re module:

# RegEx in Python
# When you have imported the re module, you can start using regular expressions:
"""
# Search the string to see if it starts with "The" and ends with "Spain":
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

"""
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""
print()

"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	  Description	                            Example	
[]	          A set of characters	                    "[a-m]"	
\	 Signals a special sequence (can also be used 
to escape special characters)	                        "\d"	
.	         Any character (except newline character)	"he..o"	
^	         Starts with	                            "^hello"	
$	         Ends with	                                "world$"	
*	         Zero or more occurrences	                "aix*"	
+	         One or more occurrences	                "aix+"	
{}	         Exactly the specified number of occurrences	"al{2}"	
|	            Either or	                            "falls|stays"	
()	        Capture and group

"""

#   []	        A set of characters     "[a-m]"
txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

print()
###################
# \	 Signals a special sequence (can also be used
# to escape special characters)
txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)
print(x)

print()
###################
# .	   Any character (except newline character)	    "he..o"
txt = "hello world"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

print()
###################
#   ^	         Starts with	                            "^hello"
txt = "hello world"

# Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

print()
###################
#  $	 Ends with	    "world$"
txt = "hello world"

# Check if the string ends with 'world':

x = re.findall("world$", txt)
if x:
    print("Yes, the string ends with 'world'")
else:
    print("No match")

print()
###################
#   *	    Zero or more occurrences	"aix*"
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print()
###################
#  +	    One or more occurrences	        "aix+"
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print()
###################
# {}	Exactly the specified number of occurrences	"al{2}"
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print()
###################
#   |	Either or	"falls|stays"
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print()
####################

