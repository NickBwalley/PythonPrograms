secret_word = "diamond"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("*********************")
print("This is a Guessing Game\nYou have 3Trials to guess\nThe Secret Word")
print("*********************")

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Your Guess: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!..")
else:
    print("YOU WIN!..")