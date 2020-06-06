vowels = ['a','e','i','o','u']
#name = input("What is your Name? ")
name = "Nicholas Bwalley"
found = [] #creating an empty list
for letter in name:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)
print("-----------------")
'''
Notes:
1. remove -> Takes an objects value as its sole argument
2. pop -> Takes an optional index as its arguments 
3. extends -> Takes a list objects as its sole arguments 
4. Insert -> Takes an index valuee and an object as its sole arguments 
5. 
'''

phrase = "Don't Panic!"
print(phrase)
plist = list(phrase)
print(plist)
new_phrase = ''.join(plist)
print(new_phrase)
print("---------------------")
phrase  = "Don't panic!"
print(phrase)
plist = list(phrase)
print(plist)
for i in range(4):
    plist.pop()
    print(plist)
plist.pop(0)
print(plist)
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
print(plist)
new_phrase = ''.join(plist)
print(new_phrase)
print("----------------------------------------------")