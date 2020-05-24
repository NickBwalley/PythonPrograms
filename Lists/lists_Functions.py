friends = ["Lashley", "Goldberg", "McIntyre", "Wyatt", "Bayley", "Sasha"]
lucky_numbers = [79,99,599,789,779,799]

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