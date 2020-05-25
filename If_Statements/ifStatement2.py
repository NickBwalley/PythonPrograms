#function
def eligible (age):
    if age >= 18:
       print("Dear " + name + " Welcome to Beers Point!... You can order any drinks...")
    else:
       print("Dear " + name + " You are Stil a Kid!... Go Back to School and Learn!...")

name = input("What is Your Name: ")
age = int(input("What is Your Age: "))
eligible (age)
