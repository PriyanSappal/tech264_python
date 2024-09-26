
str_with_extra_spaces = "   extra spaces at the start and end   "

# This is a string that has an extra three spaces at the start and end.
# Output would be:    extra spaces at the start and end

print(len(str_with_extra_spaces))

# This will output the length of the string:    extra spaces at the start and end

print(len(str_with_extra_spaces.strip()))

example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count('text'))  # The count() method counts occurrences of the substring 'text'.

# convert example_text to lowercase & print it to the screen
print(example_text.lower())  # The lower() method converts all characters to lowercase.

# convert example_text to uppercase & print it to the screen
print(example_text.upper())  # The upper() method converts all characters to uppercase.

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())  # The capitalize() method makes only the first character uppercase.

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
print(example_text.replace(' with',','))  # The replace() method substitutes the word 'with' with ','.