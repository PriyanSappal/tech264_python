
import random
import sys

dice = random.randint(1,6)
print("Welcome to the dice game!")
Y_N = input("Are you ready to play? Y/N ")

if Y_N != "Y":
    print("Go away!")
    sys.exit()

name = input("What is your name? ")
print(f"Hello, {name}! Let's roll the dice.")

user_score = 0
cpu_score = 0

while user_score < 30 and cpu_score < 30:
    input("Press Enter to roll the dice...")
    user_roll = random.randint(1,6)
    cpu_roll = random.randint(1,6)

    print(f"{name} rolled: {user_roll}")
    print(f"CPU rolled: {cpu_roll}")

    user_score += user_roll
    cpu_score += cpu_roll

    print(f"{name}'s score: {user_score}, CPU's score: {cpu_score}")

if user_score >= 30:
    print(f"Congratulations, {name}! You reached 30 and won!")
else:
    print("CPU reached 30. Better luck next time!")



