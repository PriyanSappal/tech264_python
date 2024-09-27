from math_operations import *

# Mini-calculator
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the appropriate operation based on the user's input
if operator == "+":
    result = add(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")
elif operator == "-":
    result = subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")
elif operator == "*":
    result = multiply(first_num, second_num)
    print(f"{first_num} * {second_num} = {result}")
elif operator == "/":
    if second_num != 0:
        result = divide(first_num, second_num)
        print(f"{first_num} / {second_num} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator! Please use one of +, -, *, or /.")


print("Addition")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")

print("Subtraction")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = subtract(first_num, second_num)
print(f"{first_num} - {second_num} = {result}")

print("Multiplication")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = multiply(first_num, second_num)
print(f"{first_num} * {second_num} = {result}")

print("Division")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = divide(first_num, second_num)
print(f"{first_num} - {second_num} = {result}")