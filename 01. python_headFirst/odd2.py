from datetime import datetime
import random
from time import sleep

odds = [1,3,5,7,9,11,13,15,17,19,21,
        23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,53,55,57,59]
for nick in range(5):
    right_today = datetime.today()
    right_now = right_today.minute
    if right_now in odds:
        print("This minute seems ODD!")
    else:
        print("This minute seems EVEN!")

    wait_time = random.randint(1,60)
    sleep(wait_time)
    #time.sleep(wait_time) can also be used but notice that for us to
    #use the sleep() alone, we need to define it as from time import sleep
    #which is a single package 
