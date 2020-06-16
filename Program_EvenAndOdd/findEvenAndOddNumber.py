#function to find if a number is an even number or an odd Number 
def findNumber(num):
    if(num %2 == 0 ):
        print("{0} is an Even Number".format(num))
    elif (num %2 != 0):
        print("{0} is an Odd Number".format(num))


num = int(input("Enter A Number: "))
findNumber(num)