# User story 1

# As a user, I want to be able to guess a number and know if I got it correct or not, so that I can know if
# I won or not.
import random
# Define/assign number to a variable called magic_number
magic_number = random.randint(1, 20)
attempt = 5
# Ask user for input
i = 0

# Check if this input matches magic_number
while i < attempt:
    guess = input(f"Attempt {i + 1}/{attempt} - What is your guess (Between 1 and 20)? ")

    if not guess.isdigit():
        print("Invalid input. Please enter a valid number between 1 and 20.")
        continue

    guess = int(guess)

    if guess == magic_number:
        print(f"Congratulations {magic_number} is correct!!!")
        break
    elif guess > magic_number:
        print("Your guess is high")
    else:
        print("Your guess is too low")
    i += 1
    if attempt == i and guess != magic_number:
        print(f"Sorry, all the guesses have been used up. The magic number was {magic_number}.")

# Let the user know if the response was correct or not


# Allow the user 5 guesses
