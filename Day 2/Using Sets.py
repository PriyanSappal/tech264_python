
# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Add "orange" to the fruits set using one of the set's methods.
# Print the set 'fruits' - check it's added
fruits.add("orange")
print(fruits)

# Remove "banana" from the fruits set using one of the set's methods.
# Print the set 'fruits' - check it's removed
fruits.remove("banana")
print(fruits)

# Attempt to add another "apple" to the fruits set
fruits.add("apple")

# What do you observe?
# Sets do not allow duplicates, so adding "apple" again has no effect. No duplicates will appear.

# Print the final fruits set
print("Final fruits set after attempting to add another 'apple':", fruits)

# Attempt to print the 2nd item in the set
# print(fruits[1])  # This would cause an error because sets are unordered and do not support indexing.

# Explanation:
# Sets are unordered collections, so we cannot access items by an index.
# Trying to access an item via an index (e.g. fruits[1]) will result in an error.
