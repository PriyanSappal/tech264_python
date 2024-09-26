
name = input("What is your name? ")

age = int(input("How old are you? "))

DOB = input("When were you born? ")
print(type(age))
print(f"Hi {name} you are {age} years old, your date of birth is {DOB}")

user_details_list = [name, age, DOB]
print(user_details_list)

height = float(input("What is your height in cm? "))
user_details_list.append(height)
print(user_details_list)





