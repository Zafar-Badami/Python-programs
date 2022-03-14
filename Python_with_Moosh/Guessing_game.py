guess_attempt = 1
secret_number = 9
guess_limit = 3
print(f"You have {guess_limit} attempts to guess the secret number...")
while guess_attempt <= guess_limit:
    guess=int(input(f"Attempt # {guess_attempt} Guess the number : ").strip())
    guess_attempt += 1

    if guess == secret_number:
        print ("You win !")
        break

    elif guess_attempt < 4:
        print("Wrong guess, try again")
    
else:
    print("Sorry you failed !")
