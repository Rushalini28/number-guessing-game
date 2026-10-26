
import random

print("==============================")
print("     NUMBER GUESSING GAME")
print("==============================")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"\nCongratulations! You guessed the number!")
        print(f"The secret number was {secret_number}.")
        print(f"Total attempts: {attempts}")
        break
