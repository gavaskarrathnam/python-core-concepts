'''
Comprehensions allow us to create a collection from some other iterable in a very succinct way i.e., briefly and clearly expressed.
Very often they'll save us lines and lines of code, and they help to cut down on needless boilerplate.
'''

# old style
names = ["mary", "Richard", "Noah", "KATE"]
print(f"Orignal List: {names}")
print()
processed_names = []

for name in names:
    processed_names.append(name.title())

print(f"old style iteration: {processed_names}")

# list comprehension
names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]

print(f"list comprehension: {names}")

print()
print("*** SOME OTHER EXAMPLES ***")
print()

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = []

for name, age in zip(names, ages):
	person_data = (name.title(), age)
	people.append(person_data)

print(f"Old style : {people}")
people.clear()

people = [(name.title(), age) for name, age in zip(names, ages)]

print(f"New style OR list comprehension: {people}")

'''
NOTE:  
It's also well worth noting that comprehensions are not always the right tool for the job, 
and they're not a wholesale replacement for regular for loops. 
If we have some complex logic to perform, regular loops can be much clearer, because we can break those operations up into smaller steps, 
and use variable names to signpost what is happening at various points.

None of this is possible in a comprehension, so they're generally only suitable for simpler operations.
'''

# Set Comprehension

names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}

print(f"set comprehension : {names}")

print()
# dictionary comrehension

student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for student_id, name in zip(student_ids, names):
	student = {student_id: name.title()}
	students.update(student)

print(f"Dictionary comprehension : {students}")

print()

# other way
students = {
	student_id: name.title()
	for student_id, name in zip(student_ids, names)
}

print(f"Dictionary comprehension : {students}")


## Exercise # 1
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
	squares.append(number ** 2)

print(f" squares o/p: {squares}")

print()
squares = [(n ** 2) for n in numbers]

print(f"comprehension squares o/p : {squares}")

'''
Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
'''
movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movies = {}

for key, value in movie.items():
    movies.update({key:value.title()})


print(f"Dictionary comprehension : {movies}")