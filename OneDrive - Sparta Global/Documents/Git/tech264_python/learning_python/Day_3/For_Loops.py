list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1,2,3],[4,5,6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# Loop through a list
for num in list_data:
    print(num * 2)

# Loop through the 'embedded_lists list
for data in embedded_lists:
    print(data)

# Loop through the lists embedded inside a list
for data in embedded_lists:
    print(data)
    for item in data:  # loop through the items inside the sub-list
        print(item)
print("`````````````````````````````````````````````````````````````````````````````````````````````````````````")
# Loop through a dictionary
for keys in dict_data:
    print(keys)

# Loop through a dictionary and print its values
for value in dict_data.values():
    print(value)

# Loop to print the values of the dictionary items inside a dictionary
for value in dict_data.values():
    for x in value.values():
        print(x)

# Loop to print specific values of the dictionary items inside a dictionary
for value in dict_data.values():
    print(value['money'])

for data in list_data:
    if data < 3:
        print("less than 3")
    elif data == 3:
        print("I found 3")
    else:
        print("greater than 3")