# Create a list called 'shopping_list' with the following items:
shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']

# Print the list to the screen
print("Shopping list:", shopping_list)

# Print the data type of 'shopping_list'
print("Data type of 'shopping_list':", type(shopping_list))

# Print the first item in the list
print("First item in the list:", shopping_list[0])

# Print the last item in the list
print("Last item in the list:", shopping_list[-1])

# Change the second item in the list ('bread') to 'rice' and print it to the screen
shopping_list[1] = 'rice'
print("Updated second item in the list (changed 'bread' to 'rice'):", shopping_list[1])

# Add the item 'carrots' to the list using the list's method, then check the length
shopping_list.append('carrots')  # .append() adds a single item at the end of the list
print("Shopping list after adding 'carrots':", shopping_list)
print("Length of the shopping list:", len(shopping_list))

# Add another list with two items ('toffee' and 'coffee') using the list's method
shopping_list.extend(['toffee', 'coffee'])  # .extend() adds multiple items at once
print("Shopping list after adding 'toffee' and 'coffee':", shopping_list)

# Remove 'bananas' from 'shopping_list'
shopping_list.remove('bananas')  # .remove() removes the first matching item from the list
print("Shopping list after removing 'bananas':", shopping_list)

# Remove the last item ('coffee') using the pop method
shopping_list.pop()  # .pop() removes and returns the last item by default
print("Shopping list after removing the last item ('coffee'):", shopping_list)