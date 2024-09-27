from math_operations import *

# Mini-calculator
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