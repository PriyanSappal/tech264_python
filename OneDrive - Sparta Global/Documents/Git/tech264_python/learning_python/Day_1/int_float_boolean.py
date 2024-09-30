# Integer example: An integer (int) is a whole number without any decimal point.
x = 10
print(x)          # Output: 10
print(type(x))    # Output: <class 'int'>

# Float example: A floating point number (float) is a number with a decimal point
y = 10.5
print(y)          # Output: 10.5
print(type(y))    # Output: <class 'float'>

# Boolean example
a = True

print(a)       # Output: True
print(type(a)) # Output: <class 'bool'>

# Boolean from a comparison
print(10 > 5)              # Output: True
print(5 == 5)              # Output: True
print(5 == 3)              # Output: False


One_third = 1 / 3
print(One_third)            # Output: 0.3333333333333333
print(One_third * 3)        # Output: 1.0

# Floating-point precision: Computers use binary (base-2) to represent numbers, and some decimal numbers
# (like 1/3) cannot be represented exactly in this system. As a result, floating-point numbers are stored
# with limited precision. This is why 1/3 is stored as an approximation.

# New Task: Find out what happens when you convert a string to boolean
# True is any non-empty string
# False is any empty string
b = "hello"

print(bool(b))  # Output = True

c = ""

print(bool(c))  # Output: False

