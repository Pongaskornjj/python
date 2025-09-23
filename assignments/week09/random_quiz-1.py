"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

print("=== SIMPLE GUESSING GAME ===")
print("Guess my number between 1 and 20!")
print("You have 6 attempts.")

#inputs
random_number = random.randint(1,20)

for i in range(6):
    guess_number = int(input(f"Attempt {i+1}/6 - Enter your guess:"))

    if random_number == guess_number:
        print(f"Congratulations! you won in {i+1}")
        break    
    elif random_number < guess_number:
        print("too much!")        
    else:
        print("too low!")