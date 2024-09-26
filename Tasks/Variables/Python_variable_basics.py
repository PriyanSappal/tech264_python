# What is a variable?
# Variable assigns a value that can change
# In programming, variables act as containers that store data,
# which can be used and manipulated throughout the program.

num = 5
decimal = 5.5
string = "hello"

# '=' is used to assign a value, whereas '==' is used to compare two values, checking if they are equal.
# In a dynamically typed language like Python, the type of a variable is determined at runtime,
# and you can change the type of a variable without explicitly declaring it.
# You don't need to specify the type when declaring a variable.
my_var = 10     # initially an integer
my_var = "text" # now my_var is a string

print(type(num))          # Output: <class 'int'>
print(type(decimal))      # Output: <class 'float'>
print(type(string))       # Output: <class 'str'>

print (id(num))
num = 50
print (id(num))
# The id changes because When you overwrite a variable with a new value, Python creates a new object in
# memory and assigns it to the variable.

age = input("Please enter your age here:")
print ("You are", age, "years old.")