# Learning Python

## What is a variable?
* Variable assigns a value that can change
* In programming, variables act as containers that store data,
 which can be used and manipulated throughout the program.
```python
num = 5
decimal = 5.5
string = "hello"
```


* '=' is used to assign a value, whereas '==' is used to compare two values, checking if they are equal.
* In a dynamically typed language like Python, the type of a variable is determined at runtime, and you can change the type of a variable without explicitly declaring it.
* You don't need to specify the type when declaring a variable.
```python
my_var = 10     # initially an integer
my_var = "text" # now my_var is a string
```
```python
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
```

# Understanding Operators and Operands in Python

## What is the Difference Between an Operator and an Operand?

In programming, an **operator** is a symbol that performs a specific operation on one or more operands. An **operand** is a value or variable that the operator works on. 

### Example:

- In the expression `x + y`, `+` is the operator, while `x` and `y` are the operands.

## Starting Code

```python
x = 5
y = 1
```

## Arithmetic Operators

### 1. Addition
```python
addition = x + y  # Adds x and y
print("Addition:", addition)  # Output: 6
```

### 2. Subtraction
```python
subtraction = x - y  # Subtracts y from x
print("Subtraction:", subtraction)  # Output: 4
```

### 3. Multiplication
```python
multiplication = x * y  # Multiplies x and y
print("Multiplication:", multiplication)  # Output: 5
```

### 4. Division
```python
division = x / y  # Divides x by y
print("Division:", division)  # Output: 5.0
```

### 5. Remainder (Modulus)
```python
remainder = x % y  # Finds the remainder of x divided by y
print("Remainder:", remainder)  # Output: 0
```

## Comparison Operators

### 1. Greater Than
```python
greater_than = x > y  # Checks if x is greater than y
print("Greater Than:", greater_than)  # Output: True
```

### 2. Less Than
```python
less_than = x < y  # Checks if x is less than y
print("Less Than:", less_than)  # Output: False
```

### 3. Equal
```python
equal = x == y  # Checks if x is equal to y
print("Equal:", equal)  # Output: False
```

### 4. Not Equal
```python
not_equal = x != y  # Checks if x is not equal to y
print("Not Equal:", not_equal)  # Output: True
```

### 5. Greater Than or Equal To
```python
greater_than_equal = x >= y  # Checks if x is greater than or equal to y
print("Greater Than or Equal To:", greater_than_equal)  # Output: True
```

### 6. Less Than or Equal To
```python
less_than_equal = x <= y  # Checks if x is less than or equal to y
print("Less Than or Equal To:", less_than_equal)  # Output: False
```

# Understanding Numeric Data Types and Boolean Data Type in Python

## Numeric Data Types: `int` and `float`

### `int` (Integer)
- Represents whole numbers without a fractional part.
- Examples: `-3`, `0`, `42`, `1000000`
- They can be positive or negative.

**Demonstration:**
```python
# Example of integer operations
a = 10
b = 3
print("Integer Addition:", a + b)        # Outputs: 13
print("Integer Subtraction:", a - b)     # Outputs: 7
print("Integer Multiplication:", a * b)  # Outputs: 30
print("Integer Division (floor):", a // b) # Outputs: 3
```

### `float` (Floating Point)
- Represents real numbers, which can have a fractional part.
- Examples: `3.14`, `-0.001`, `2.0`, `-42.5`
- They can be expressed in decimal form or using scientific notation (e.g., `1.5e2` which means `150`).

**Demonstration:**
```python
# Example of floating-point operations
x = 10.5
y = 3.2
print("Float Addition:", x + y)         # Outputs: 13.7
print("Float Subtraction:", x - y)      # Outputs: 7.3
print("Float Multiplication:", x * y)   # Outputs: 33.6
print("Float Division:", x / y)          # Outputs: 3.28125
```

## Boolean Data Type
- The boolean data type has two possible values: `True` and `False`.
- It's often used in conditional statements and logical operations.

**Demonstration:**
```python
# Example of boolean operations
a = 10
b = 20

is_a_greater = a > b          # False
is_b_equal_to_20 = (b == 20)  # True

print("Is A greater than B?", is_a_greater)  # Outputs: False
print("Is B equal to 20?", is_b_equal_to_20) # Outputs: True

# Logical operations
print("Is A less than B and B equal to 20?", is_a_greater and is_b_equal_to_20)  # Outputs: False
print("Is A less than B or B equal to 20?", is_a_greater or is_b_equal_to_20)    # Outputs: True
```

## Explanation of Floating Point Precision Issue
When you execute the following code:

```python
One_third = 1 / 3
print(One_third)           # Outputs: 0.3333333333333333
print(One_third * 3)      # Outputs: 1.0
```

You might expect that multiplying `0.3333333333333333` by `3` would yield exactly `1`. However, due to the nature of floating-point arithmetic, this isn't guaranteed.

### 1. Floating-Point Representation
- Computers use binary (base 2) representation for numbers, which can lead to inaccuracies when representing certain decimal fractions.
- For example, `1/3` is a repeating decimal (`0.333...`) that cannot be perfectly represented in binary. It is approximated, leading to small errors.

### 2. Rounding Errors
- When you multiply `One_third` by `3`, the result may not be exactly `1` due to these small errors in representation, but Python rounds it to `1.0` for display.

## Lesson to Learn
1. **Understanding Precision**:
   - Be aware that floating-point numbers are not always exact. When doing arithmetic with them, results can be slightly off from expected values.
   
2. **Using Decimal for Precision**:
   - For financial and other precision-critical applications, consider using the `Decimal` type from the `decimal` module, which provides better precision for decimal numbers.

   **Example of using `Decimal`:**
   ```python
   from decimal import Decimal

   one_third_decimal = Decimal(1) / Decimal(3)
   print(one_third_decimal)           # Outputs: 0.3333333333333333333333333333
   print(one_third_decimal * 3)      # Outputs: 1.0
   ```

# **None in Python**

* In Python, None is a special constant that represents the absence of a value or a "null" value.
* It is often used to indicate that a variable has no value or that a function does not explicitly
return anything.
* It is commonly used when you want to initialise a new variable with no initial value, when no argument
has passed and as a default return value.
* In other languages it can be none as null. 


### Converting None to a boolean

```python
x = None
print(bool(x))  # Output: False

# 1. Assign x to be None
x = None

# 2. Print whether x is equal to None
if x is None:
    print("x is None")  # This will print
else:
    print("x is not None")
```

# String Method Checks

This document outlines the checks performed on the string `hi = "Hello World!"` using various string methods. Each method returns a boolean value (True or False) without using any `if` statements.

```python
hi = "Hello World!"

# Check if 'hi' is made up of letters only
print(hi.isalpha())  # True if all characters are letters

# Check if 'hi' is made up only of lowercase letters
print(hi.islower())  # True if all characters are lowercase

# Check if 'hi' is made up only of uppercase letters
print(hi.isupper())  # True if all characters are uppercase

# Check if 'hi' ends with an exclamation mark
print(hi.endswith('!'))  # True if string ends with '!'

# Check if 'hi' starts with a capital "H"
print(hi.startswith('H'))  # True if string starts with 'H'
```
# Day 2 Tasks: [Task Day2](Task_Day2.md)
# Day 3 Tasks: [Control Flow](Control_Flow.md)
