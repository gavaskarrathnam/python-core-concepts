# hourly_wage = input("Please enter your hourly wage: ")
# hours_worked = input("How many hours did you work this week? ")
#
# print("Hourly wage: " + hourly_wage)
# print("Hours worked: " + hours_worked)

# exercises

# 1. Using the variable below, print "Hello, world!".
greeting = "Hello, world"
exclamation = "!"
print("{}{}".format(greeting, exclamation))
print(f"{greeting}{exclamation}")
print("{}!".format(greeting))

print("gavasKAR RATHnam".capitalize())
print("gavasKAR RATHnam".title())


# 2. Ask the user for their name, and then greet the user, using their name as part of the greeting.
# The name should be in title case, and shouldn't be surrounded by any excess white space.
# For example, if the user enters "lewis ", your output should be something like this:
name = input("Please enter your name: ").strip().title()
print("Hello, {} !".format(greeting))

# 3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
print("I am " + str(40))

# 4. Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print("{} ({}), directed by {}".format(title, release_year, director))
# Remember that everything inside the curly braces is considered code for an f-string,
# and each value we want to interpolate should be in its own set of curly braces.
print(f"{title} ({release_year}), directed by {director}")


# mini project
# https://blog.tecladocode.com/python-30-day-3-project/

# Regina George earned $800 this week.
employee_name = input("Please Employee Name: ").strip().title()
hourly_wage = float(input(f"Please enter {employee_name}'s hourly wage: "))
work_hours = float(input(f"Please enter {employee_name} work hours this week: "))
week_net_income = "{:.2f}".format(hourly_wage * work_hours)

print(f"{employee_name} earned ${week_net_income} this week")


age = [2,3,4]
ages = "Ages {}".format(age)
print("Ages ", ages)



