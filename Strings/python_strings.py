# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')
a = "Hello"
print(a)
# multiline string
# Note: you can use single triple quotes or triple double quotes to denote a multiline string
a = '''Welcome to the best 
Hotel in Houston Texas 
Here you can get good seafood'''
print(a)
print()
# String Arrays
a = "Hello World"
print(a[0])
print()
# looping through String
for x in "banana":
    print(x)

# check string
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)  # return boolean true if its there or false if not
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes", "free" " is present") # prints only if free is present

# check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)  # returns boolean
# using if statement
if "expensive" not in txt:
    print("expensive", " not in txt")

print("-----------------------------------")
# \n the escape sequence used to print to a new line
print("My name is NickBwalley\nI am a Coder")
# Prints a quotation mark on bronze Bomber word
print("Also Called the \"Bronze_Bomber\"")
phrase = "PYCharm"
print(phrase + " Is a cool IDE")  # basically concatenations
print(phrase.lower())  # converts the phrase variable to lowerCase
print(phrase.upper())  # converts the phrase variable to upperCase
print(phrase.isupper())  # function to check if the phrase variable is uppercase returns false if not
print(phrase.islower())  # function to chek if the phrase variable is lowerCase returns false if not
print(phrase.upper().isupper())  # converts the string to upperCase then returns True
print(phrase.lower().islower())  # converts the string to lowercase then returns True
print(len(phrase))  # outputs the length of a string defined in your variable that is
print(phrase[0])  # output the first letter inside our variable phrase >> it will start at 0 index
print(phrase.index("rm"))  # returns the index of the variable string
print(phrase.replace("PYCharm", "NickBwalley"))  # function to replace a value with another
