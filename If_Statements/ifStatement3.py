name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))

def check_age(age):
    if age >=1 and age <=17:
        print("Dear "+name+ " You are Still a Kid!..Go Finish School First!..")
    elif age >=18 and age <=21:
        print("Dear " + name + " You are Now an Adult!.. You are fit to have a National ID!..")
    elif age >=22 and age <=35:
        print("Dear " + name + " You are fit to Join a Driving School and Start Driving!..")
    elif age >=36 and age <=50:
        print("Dear " + name + " You are fit to Join the Army and Work for the Country!..")
    elif age >= 50 and age <= 100:
        print("Dear " + name + " You are Old!.. Please Retire and Earn Pension!..")
    else:
        print("Invalid Age!..Please Try again...")

check_age(age)
