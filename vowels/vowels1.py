#printing out the vowels in your name
vowels = ['a','e','i','o','u']
#getting input from the user
myName = input("What is Your Name: ")
#for loop to check vowels from name
for letter in myName:
    if letter in vowels:
        print(letter)