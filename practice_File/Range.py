
word = "bottles"
for beer_num in range(5,0,-1):
    print(beer_num, word, " of beer on the Wall")
    print(beer_num, word, "of beer")
    print("Take one \n Pass it around")
    if beer_num == 1:
        print("No more bottles of Beer on the Wall!..")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word  = "bottle"
        print(new_num, word, " of beer on the wall!..")
        print()