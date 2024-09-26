pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.3f}")  # The .3f specifies 3 decimal places.

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 5 decimal places: {pi:.5f}")  # The .5f specifies 5 decimal places.

score = 16
max_score = 26
score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")  # Prints the raw decimal value of score_as_decimal.

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal * 100}%")  # Multiplies by 100 to get the percentage.

# Use an f-string to print 'score_as_decimal' formatted as a percentage rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal * 100:.2f}%")  # The .2f rounds the percentage to 2 decimal places.
print(f'You scored {score_as_decimal:.2%}')  # This is an easier method
# Use an f-string to print 'score_as_decimal' formatted as a percentage rounded to a whole number e.g. 'You scored 62%'
print(f"You scored {score_as_decimal * 100:.0f}%")  # The .0f rounds the percentage to a whole number.
print(f'You scored {score_as_decimal:.0%}')
