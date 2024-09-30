Hw = "Hello world!"

print(Hw)  # Print the string "Hello world!"

# Find out how many characters Hw has
print(len(Hw))  # The len() function returns the number of characters in Hw, which is 12 in this case.

# Get the character in the first position in Hw
print(Hw[0])  # Access the first character, 'H', using index 0.

# Get the last character
print(Hw[-1])  # Access the last character, '!', using index -1.

# Get the 2nd last character
print(Hw[-2])  # Access the second-to-last character, 'd', using index -2.

# Write a comment to EXPLAIN what does this do
print(Hw[2:])  # This prints the string starting from the character at index 2 ("llo world!").

# Write a comment to EXPLAIN what does this do
print(Hw[-3:])  # This prints the last three characters of the string, starting from index -3 ("ld!").

# Write a comment to EXPLAIN what does this do
print(Hw[:5])  # This prints the first five characters, starting from index 0 to index 4 ("Hello").

# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[1:5])  # This prints the substring from index 1 up to (but not including) index 5 ("ello").

print(Hw[::-1])