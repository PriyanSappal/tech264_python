# Initialise x with the value of 0 
x = 0
while x < 10:
    print(f"{x}")
    x += 1

# If you remove the line x = 0, the code will raise a NameError because x is not defined when the while loop starts.
# Python requires variables to be initialized before they are used.

# If you don't increment x (remove the line x += 1), the loop will run infinitely because x will never change,
# and the condition x < 10 will always be True.
print("``````````````````````````````````````````````````````````````````````````````````````````````````````````````")
# Second while loop: Stops when x equals 4
x = 0  # Re-initialize x with 0

while x < 10:  # Loop while x is less than 10
    print(f"x => {x}")
    if x == 4:
        break  # Exit the loop when x is 4
    x += 1  # Increment x by 1