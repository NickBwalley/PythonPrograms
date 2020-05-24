vowels = ['a','e','i','o','u']
#get user input
myName = input("What is your Name: ")
found = []
#creating a forloop to print out vowels without duplicates
for output in myName:
    if output in vowels:
        if output not in found:
            found.append(output)
for result in found:
    print(result)