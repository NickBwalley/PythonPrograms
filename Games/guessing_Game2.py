secret_word = "Silver"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("-----------------------------------------------")
print("Guessing Game: Hint(Arg): You Have 3Trials:")
print("-----------------------------------------------")
while guess != secret_word and not(out_of_guesses):
    if(guess_count < guess_limit):
        guess = input("Guess the Secret Word: ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!...")
else:
    print("YOU WIN!...")