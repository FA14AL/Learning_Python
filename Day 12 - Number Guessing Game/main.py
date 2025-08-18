from art import logo
import random
print(logo)
user_difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard':").lower()
number = random.randint(1,100)
print(number)


if user_difficulty == 'easy':
    for i in range (1,11):
        attempts_left = 10 - i + 1
        users_guess = int(input(f"You have {attempts_left} attempts remaining to guess the number.\nMake a guess:"))

        if users_guess == number:
            print(f"You got it! The answer was {number}.")
            break

        if attempts_left == 1:
            print("You've run out of guesses. Refresh the page to run again.")

        elif users_guess > number:
            print("Too high.\nGuess again.")
        elif users_guess < number:
            print("Too low.\nGuess again.")

if user_difficulty == 'hard':
    for i in range (1,6):
        attempts_left = 5 - i + 1
        users_guess = int(input(f"You have {attempts_left} attempts remaining to guess the number.\nMake a guess:"))

        if users_guess == number:
            print(f"You got it! The answer was {number}.")
            break

        if attempts_left == 1:
            print("You've run out of guesses. Refresh the page to run again.")

        elif users_guess > number:
            print("Too high.\nGuess again.")
        elif users_guess < number:
            print("Too low.\nGuess again.")
