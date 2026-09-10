secret_number = 7
attempts = 0

print("Guess the secret number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break

print(f"You got it in {attempts} tries!")