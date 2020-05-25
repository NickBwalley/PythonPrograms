
is_male = False
is_tall = True
if is_male and is_tall:#when using the and operator both conditions have to be true for the condition to return a true
    print("You are a Tall Male!")
elif is_male and not(is_tall):
    print("You are a Short Male")
elif not(is_male) and is_tall:
    print("You are Tall but You are a Female!")
else:
    print("You are Neither Male nor Tall!")

