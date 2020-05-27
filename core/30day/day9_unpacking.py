# '''
# Day 9: Unpacking, Enumeration, and the zip Function
#
# 'unpacking' is really useful iteration technique. We're also going to be exploring a couple of new functions: enumerate and zip.
# '''
#
# # restrictions
# movie = ("12 Angry Men", "Sidney Lumet", 1957)
#
# # way #1
# title = movie[0]
# director = movie[1]
# year = movie[2]
# print(f"title : {title}, director : {director}, year : {year}")
#
# print(" ")
#
# # way #2
# title, director, year = movie # no. of elements should mach with no. of assignment variable otherwise get exception
# print(f"title : {title}, director : {director}, year : {year}")
#
# print(" ")
#
# print(" ")
# # dynamic way
# movies = [
# 	(
# 		"Eternal Sunshine of the Spotless Mind",
# 		"Michel Gondry",
# 		2004
# 	),
# 	(
# 		"Memento",
# 		"Christopher Nolan",
# 		2000
# 	),
# 	(
# 		"Requiem for a Dream",
# 		"Darren Aronofsky",
# 		2000
# 	)
# ]
#
# for title, director, year in movies:
# 	print(f"{title} ({year}), by {director}")
#
# print(" ")
#
# print(" Why we go for Enumeration ")
# '''
# Enumeration:
# One common application for unpacking is when using a function called enumerate.
# '''
#
# # Problem: movies list print in following manner
# '''
# 1. Eternal Sunshine of the Spotless Mind (2004), by Michel Gondry
# 2. Memento (2000), by Christopher Nolan
# 3. Requiem for a Dream (2000), by Darren Aronofsky
# '''
#
# for counter, (title, director, year) in enumerate(movies, start=1):
#     print(f"{counter}. {title} ({year}), by {director}")
#
# print(" ")
# print(" ZIP function ")
# '''
# The zip function
# zip is an extremely powerful and versatile function used to combined two or more iterables into a single iterable.
# '''
# pet_owners = ["Paul", "Andrea", "Marta"]
# pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
# city = ["SF", "NY", "NJ"]
#
# #combine with 'zip + enumerator'
# pets_and_owners = list(zip(pet_owners, pets, city))
# print(" raw list : ")
# print(pets_and_owners)
#
# print("list with format :")
# for owner, pet, city in pets_and_owners:
#     print(f"{owner} owns {pet} lives in {city}.")
#
# print(" ")

# exercise - 1

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# #expected o/p : BoJack Horseman is a horse voiced by Will Arnet.

for movie, voiceby, character in main_characters:
    print(f"{movie} is a {character.lower()} voiced by {voiceby}")

print(" ")
print(" ")

# exercise - 2
'''
Unpack the following tuple into 4 variables:
("John Smith", 11743, ("Computer Science", "Mathematics"))
'''

tpl = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, zipcode, (sub1, sub2) = tpl
print(f"{name} >> {zipcode} >> {sub1} >> {sub2}")

print(" ")
print(" ")

# exercise - 3
# Investigate what happens when you try to zip two iterables of different lengths.
# For example, try to zip a list containing three items, and a tuples containing four items.
name_list = ["a", "b", "c"]
age_tpl = (40, 38, 41, 45)

name_and_age = list(zip(name_list, age_tpl))

print("combine ZIP + unpacking :")
print(name_and_age)
for name, age in name_and_age:
    print(f"{name} old is {age}.")

print(" ")

print("without loosing the items:")
# without loosing collection
from itertools import zip_longest
no_loose_data = list(zip_longest(name_list, age_tpl, fillvalue="-"))
for newname, newage in no_loose_data:
    print(f"{newname} old is {newage}.")
