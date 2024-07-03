#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num = random.randint(1, 100)
    rounds = 0

    while rounds < 5:
        guess = input("Guess a number between 1 and 100\n> ")

        # Check if the input is a digit
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("Correct!")
            break

        rounds += 1

    if rounds == 5 and guess != num:
        print(f"Sorry, you've used all your attempts. The correct number was {num}.")

if __name__ == "__main__":
    main()

