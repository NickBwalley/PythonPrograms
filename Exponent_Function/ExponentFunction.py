
print(2**3) #same as 2^3

#function to raise_number_to_power
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))#from function raise_to_power

def power_function(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
baseNumber = int(input("Enter Base Number: "))
powerNumber = int(input("Enter Power Number: "))
print(power_function(baseNumber, powerNumber))