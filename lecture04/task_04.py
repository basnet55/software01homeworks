import random

random_number = random.randint(1,10)
print("Guess the number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))

    if guess > random_number:
        print("Too high! Try again")
    elif guess < random_number:
        print("Too low! Try again")
    else:
        print("Correct! You guessed it!")
        break