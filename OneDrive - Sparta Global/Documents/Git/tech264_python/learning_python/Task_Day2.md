# Learning Python Day 2 

### Task: [Slice_string](Day_2/Slice_string.py)

What is slicing strings?
* Slicing strings is when you are extracting a portion of the string (substring) by specifying a certain range. 
* It will follow this syntax```string[start:end]```.
    * The start is the index of the first character (0 is the first character of the string)
    * The end is the index after the last character you want to include. 
    * You can also have negative indices, which will count from the end. 

### Task: [Use String Methods](Day_2/Use_String_Methods.py)

### Task:[Concatenates_with_diff_data_types.py](Day_1/Concatenates_with_diff_data_types.py)
* Concatenation is the process of joining two or more strings together using the + operator in Python. When you concatenate strings, you combine them into a single, larger string. This is often used to create more readable or dynamic text.

### Task: [f-string](Day_3/f-string.py)
* f-string allows you to put variables in without having to use commas and quotation marks to separate. 
* f"Pi to 3 decimal places: {pi:.3f}" formats the pi value to 3 decimal places (.3f).
* f"You scored {score_as_decimal}" directly prints the decimal value without formatting.
* f"You scored {score_as_decimal * 100}%" multiplies score_as_decimal by 100 to convert it to a percentage.
* `f"You scored {score_as_decimal * 100:.2f}%" rounds the percentage to 2 decimal places.
* `f"You scored {score_as_decimal * 100:.0f}%" rounds the percentage to a whole number.

### Task: [Convert String to int and float](Day_1/Convert_String_to_int_and_float.py)

### Task: [Working with Lists](Day_2/Lists.py) []

### Task: [Name, Age and DOB](Name_Age_DOB.py)

### Task: [Mix all the data about a user into a list](Day_2/Mix_data_into_a_list.py)

### Task: [Tuples](Day_2/Tuples.py) ()
* Both Tuples and lists are similar as they can hold multiple items, including strings, numbers, or even other collections.
* Tuples are immutable. This means that once a tuple is creates, its elements cannot be changed in any way. 
* Data types that are immutable: 
  * Strings
  * Integers
  * Floats
  * Booleans 
  * Frozen Sets
* Tuples are useful when you want to store a collection of items that should not change (e.g. storing coordinates)
* The code below will create a tuple with the items and prints the tuple. Finally, it will count how many times bread has been counted. 
```python
essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
```

### Task: [Dictionaries](Day_2/Dictionaries.py) {"x": "y"
}
* A dictionary saves data in key-value pairs. Each value is associated with a unique key. 
* The key acts as a label, and the value can be any data type (string, list, integer, etc.). 
* Each key must be unique, and values are accessed by referencing their corresponding key.

### Task: [Using Sets](Day_2%2FUsing_Sets.py)  {}
* A set is an unordered collection of unique elements.
* Two ways in which it is different from a tuple and list:
1) Sets automatically remove duplicate items.
2) Sets are unordered, whereas lists and tuples are ordered. 

### Task: [Frozen Sets](Day_2/Frozen_set.py)
* A Frozen Set is a type of collection that is immutable and therefore cannot be changed after being created. 
* Hashable: You are able to add a frozen set to a normal set.
* Differences between a normal set and a frozen set: 
  * Mutability: The main difference is that frozen sets are immutable, meaning once they are created, you cannot change them. Normal sets are mutable, allowing you to add, remove, or modify elements after creation.
  * Use Cases: Frozen sets are useful when you need to ensure that the data will not change (e.g., as keys in dictionaries or when adding sets to other sets). Normal sets are useful when you need a collection of unique items that can be updated.

### If time: Task: [Waiter Helper List](Day_2/Waiter_helper_list.py)


