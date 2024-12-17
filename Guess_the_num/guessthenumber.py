# Project 2 : Guess the number game by computer
# 1 to 100 numbers.

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I am think a random number between 1 and 100.")
    print("Try to guess it!")

    # Loop until the user guesses the number
    while True:
        try:
            # Ask the user to guess the number
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the user's guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break  # End the game when the correct number is guessed

        except ValueError:
            print("Please enter a valid integer.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
