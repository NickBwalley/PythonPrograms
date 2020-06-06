vowels = ['a','e','i','o','u']
name = input("What is your Name? ")
found = [] #creating an empty list
for letter in name:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)