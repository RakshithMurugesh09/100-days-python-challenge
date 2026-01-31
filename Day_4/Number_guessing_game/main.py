import random

secret_number = random.randint(1,10)

attempt = 0
game = True
while game:
    guess_number = int(input("\nGuess the number (1-10): "))
    attempt += 1
    if guess_number == secret_number:
        print(f"You guessed it right in {attempt} attempts!")
        game = False
    elif guess_number > secret_number:
        print("Guess number is greater than Secret number\nTry again!!!!")
    else:
        print("Guess number is less than Secret number\n Try again!!!!")
