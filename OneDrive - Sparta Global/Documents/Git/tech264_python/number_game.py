# User story 1

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# Define/assign number to a variable called magic_number
magic_number = 7
attempt = 5
# Ask user for input
user_input = int(input("please enter your guess")
i = 0
while attempt > i:
# Check if this input matches magic_number
if user_input != magic_number:
    print("please try again")
        if user_input > magic_number:
            print ("Too high")
        elif user_input < magic_number:
            print("Too low")

        else:
            print("You won")



# Let the user know if the response was correct or not


# Allow the user 5 guesses


# User story 2

# As a user, I want to be able to guess a number and know if I need to go higher or lower.


# User story 3

# As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.


# User story 4

# As a user, after each guess, I would like to know how many guesses I have left.





# User story 5

# As a user, I would like the magic to be randomly generated each time I play so it is more fun.


# User story 6

# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.