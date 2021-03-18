#The Beer song
#/*******************************************************/
#Assigns the value bottles (string) and assigns to the new varible word
word = "bottles"
#Loop a specific number of times from 99 down to none which steps from -1
#beer_num is the loop iteration varible
for beer_num in range(4, 0, -1):
    #four calls to the print function displays the current iteration's song lyrics
    print(beer_num, word, "of beer on the wall.")

    print(beer_num, word, "of beer.")

    print("Take one down.")

    print("Pass it around.")

    if beer_num ==1:
        print("No more bottles of beer on the wall")
    else:
        #creates a new variable called new_num and performs a mathematical operation
        #whereby it takes the beer_num then subtracts -1 to assign the new varible
        #to the older varible
        new_num = beer_num -1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")    
    print()
    
    
