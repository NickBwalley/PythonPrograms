from datetime import datetime

odds = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,
        39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("Minute is in odds!")
else:
    print("Minutes is even!")
#this is the most preferred means to use in invoking methods by programmers    
time_now = datetime.today()
right_this_minute = time_now.minute
