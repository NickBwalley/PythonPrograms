
mySwitch = {
    1: "You Love ladies who Smoke",
    2: "You Love Drinking Chrome",
    3: "You Love ladies who Drink",
    4: "You Love Reading Novels",
    5: "You Love Partying"
}
#take user Input
num = int(input("Choose a Number>>(1-5): "))
print(mySwitch.get(num,"Invalid Input"))