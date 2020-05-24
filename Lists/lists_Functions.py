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