# Task 1:

# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")

# PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit() and int(age) <= 117:
        # SET user_prompt TO FALSE
        user_prompt = False
    # ADD ELSE STATEMENT HERE
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Please enter your age in digits only and an age that is not that old(e.g., 20).")


print(f"Your age is {age}")