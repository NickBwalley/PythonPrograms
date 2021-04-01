friends = ["Lashley", "Goldberg", "McIntyre", "Wyatt", "Bayley", "Sasha"]
lucky_numbers = [79, 99, 599, 789, 779, 799]

friends.extend(lucky_numbers)#combines the first and the second list
print(friends)
friends.append("Undertaker")#adds another element at the end of the list
print(friends)
friends.insert(1,"Lana")#adds the element at the index1
print(friends)
friends.remove("Lashley")#removes the element from the list
print(friends)
friends.clear() #removes everthing from the list
print(friends)
friends.append("RandyOrton")
friends.append("KeithLee")
friends.append("TommassoCiampa")
friends.append( "JohnnyGargano")
print(friends)
friends.pop()#pops the last element of the list
print(friends)
print(friends.index("KeithLee"))#prints the index of the item in the list
friends.append("RandyOrton")
print(friends.count("RandyOrton"))#counts the number of times "RandyOrton" Appears in the List
friends.sort()#sorts the list in alphabetical order
print(friends)
lucky_numbers.sort()#sorts the numbers in ascending order
print(lucky_numbers)
friends2 = friends.copy()#makes a copy of the original friends
print(friends2)
friends2.remove("TommassoCiampa")#removes the entity from the list
print(friends)
print(friends2)