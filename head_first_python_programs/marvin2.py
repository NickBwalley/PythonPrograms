paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char) #this line tabs only once in running this code
print()#this line is just for adding a whitespace below the output(like: <br>)
for char in letters[-7:]:
    print('\t'*2, char)#the *2 is used to tab the output twice in the operation
print()
for char in letters[12:20]:
    print('\t'*3, char)#the *3 is used to tab the output thrice in the operation
print()
