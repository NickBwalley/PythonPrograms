#program to find a vowel in a word
#declare a list with the vowels
vowels = ['a','e','i','o','u']
#create another variable called word and assign it a value
word = "Milliways"
#creating a loop with a loop iteration variable called "Letter"
for letter in word:
    if letter in vowels:
        print(letter)

        
