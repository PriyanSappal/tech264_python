
starters = ["Fries", "Soup", "Salad", "Bread"]

mains = ["Pizza", "Pasta", "Pie"]

desserts = ["Ice Cream", "Cake", "Brownie"]

# Greet the user
print("Hello and welcome to our Restaurant")

# Print a list of starters
# Take an input for the user for their starter
print(starters)
starter = input("Please select a starter. ")
while starter not in starters:
    print("Please try again.")
    print(starters)
    starter = input("Please select a starter. ")
# Print a list of mains
# Take an input for the user for their main course
print(mains)
main = input("Please select a main. ")

# Take an input for the user for their dessert
# Print all of the user's choices
print(desserts)
dessert = input("Please select a dessert. ")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = [starter, main, dessert]
print(f"Here is your order: {starter}, {main}, {dessert}")

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
prices = {
    "Fries": 5, "Salad": 4, "Soup": 6, "Bread": 5,
    "Pie": 15, "Pasta": 12, "Pizza": 10,
    "Ice Cream": 5, "Brownie": 6, "Cake": 7
}
total_bill = prices[starter] + prices[main] + prices[dessert]
print(f"Your total is £{total_bill}.")

