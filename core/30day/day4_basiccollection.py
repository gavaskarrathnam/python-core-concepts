#list

numbers = [1, 2, 4, 5] # number 3 missing
numbers.insert(2, 3)   # inserting number 3 in the middle between 2, 4
print(numbers)


names = ["gavaskar", "rathnam", "taanve", "krishna"]
names = names + ["ramya"]
print(names)
names.append("rajeswari")
print(names)
names.insert(5, "karthik")
print(names)
names.append("rathnam")
print(names)

# delete options
print("*** delete options ***")
names = ["John", "Sarah", "Alice", "Mike"]
names.remove("Sarah")
print(names)
del names[1]
print(names)

names = ["John", "Sarah", "Alice", "Mike"]
last_in_line = names.pop()

print(names)         # ['John', 'Sarah', 'Alice']
print(last_in_line)  # Mike

names = ["John", "Sarah", "Alice", "Mike"]
names.pop()

print(names)  # ['John', 'Sarah', 'Alice']
names.pop(1)
print(names)  # ['John', 'Alice']


names = ["John", "Sarah", "Alice", "Mike"]
names.clear()
print(names)

print("*** Tuple ***")
# Tuple
# Much like with lists, tuples are ordered collections,
# where each item can be accessed by index based on their position in the collection.
names = ("gavaskar", "rathnam", "taanve")
print(names)

'''
This means you won’t find any pop or append methods for tuples, and the del keyword isn’t going to allow you to remove values using an index.
One thing that will work is the + operator, but if we remember back to our discussion of + with lists, this operator gives us a new collection. If we use it with a tuple, the original tuple is going to remain unchanged: we’ve just created a new one.
Note that you can only use + to join two tuples.
'''

movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004,
        "$500 M"
	),
	(
		"Memento",
		"Christopher Nolan",
		2000,
        "$200 M"
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000,
        "$100 M"
	)
]
print(movies)
print(movies[0])
print(movies[0][0])

#otherwise
movie = movies[0]
print("Movie tuple: ", movie)
print(f"Movie name: {movie[0]}")

# Exercises
ex_movies = [
	(
		"Califonia Guy",
		"Michel Gondry",
		2004,
        "$500 M"
	)
]

move_name = input("Enter the movie name: ")
director = input(f"Enter the {move_name}'s director name: ")
release_year = int(input(f"Enter the {move_name} release year: "))
budget = input(f"Enter the {move_name} budget: ")

ex_movies.append( (move_name, director, release_year, budget) )
print(ex_movies)
