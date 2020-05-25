
is_male = True
is_tall = False
if is_male and is_tall:#when using the and operator both conditions have to be true for the condition to return a true
    print("You are a Tall Male!")
elif is_male and not(is_tall):
    print("You are a Short Male")
else:
    print("You are Neither Male nor Tall!")

