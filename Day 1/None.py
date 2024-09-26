# In Python, None is a special constant that represents the absence of a value or a "null" value.
# It is often used to indicate that a variable has no value or that a function does not explicitly
# return anything.

# It is commonly used when you want to initialise a new variable with no initial value, when no argument
# has passed and as a default return value.

# In other languages it can be none as null

# Converting None to a boolean
x = None
print(bool(x))  # Output: False

# 1. Assign x to be None
x = None

# 2. Print whether x is equal to None
if x is None:
    print("x is None")  # This will print
else:
    print("x is not None")
