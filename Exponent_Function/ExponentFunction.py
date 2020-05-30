
print(2**3) #same as 2^3

#function to raise_number_to_power
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3, 3))#from function raise_to_power