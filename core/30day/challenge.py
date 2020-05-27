#how to give input in BOLD

import colorama

print(colorama.Style.BRIGHT)

name = input("Name: ")
age = input("Age: ")

print(colorama.Style.RESET_ALL)

print("Hi " + name + " (age) " + age)

