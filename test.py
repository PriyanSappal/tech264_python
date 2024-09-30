# this is for revision purposes
# dictionaries

dict = {"fruit": "apple",
        "price": 4,
        "colour": "red"
        }

print(dict)
print(type(dict))
print(dict.keys())
print(dict.values())

print(dict["fruit"])

dict["colour"] = "green"
print(dict)


# lists

# sets

num_set = {1, 2, 3, 4}
print(type(num_set))
frozen_num = frozenset({5, 6, 7})
print(frozen_num)
print(type(frozen_num))

num_set.add(frozen_num)
print(num_set)

# functions
# Write a Python function to find the maximum of three numbers.


def maximum(a, b, c):
        return max(a, b, c)


print(maximum(2, 3, 5))

# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def my_sum(numbers: list):
        return sum(numbers)



print(my_sum([1,2,3,4]))



def times(number):
    result = 1  # Start with 1 since it's the neutral element for multiplication
    for num in number:
        result *= num  # Multiply each number in the list
    return result

# Correct function call
print(times([2, 3, 4]))  # Output: 24


# Write a Python program to reverse a string.

def redrum(string: str):

    return string[::-1]

print(redrum("hello what is your name"))


# Function to Find the Largest Number
def find_largest(list: list):
    return max(list)


print(find_largest([2, 3, 5, 8, 15]))

# Function to Calculate the Factorial
def factorial(n):
    result = 1
    for n in range(1, n+1):
        result *= n
    return result


print(factorial(5))


# function to count vowels in a string

def count_vowels(phrase: str):
    vowels = "a,e,i,o,u"
    count = 0
    for char in phrase:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello world"))


def sum_dict_values(dictionary: dict):
     return sum(dictionary.values())



my_dict = {'a': 10, 'b': 20, 'c': 30}
print(sum_dict_values(my_dict))


# If statements

def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


check_even_odd(4)
check_even_odd(7)



def max_of_three(a: int, b: int, c: int):
    return max(a, b, c)


print(max_of_three(10, 20, 30))



def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(2020))
print(is_leap_year(1999))
print(is_leap_year(2024))

def add_until_100():
    total = 0
    while total < 100:
        num = int(input("Enter a number: "))
        total += num
        print(f"Current total: {total}")
    print(f"The sum is {total}")


add_until_100()