'''
What are first class functions?
A programming language is said to have first class functions when functions in that language are treated like any other type.
They're said to be "first class citizens" of the language.
'''

# simple exmple
# def get_grade_average(student):
# 	return student["grade_average"]
#
#
# students = [
# 	{"name": "Hannah", "grade_average": 83},
# 	{"name": "Charlie", "grade_average": 91},
# 	{"name": "Peter", "grade_average": 85},
# 	{"name": "Rachel", "grade_average": 79},
# 	{"name": "Lauren", "grade_average": 92}
# ]
#
# valedictorian = max(students, key=get_grade_average)
# print(valedictorian)

# print()
#
# # simple command-pattern
# def add(a, b):
# 	print(a + b)
#
#
# def subtract(a, b):
# 	print(a - b)
#
#
# def multiply(a, b):
# 	print(a * b)
#
#
# def divide(a, b):
# 	if b == 0:
# 		print("You can't divide by 0!")
# 	else:
# 		print(a / b)
#
#
# operations = {
# 	"a": add,
# 	"s": subtract,
# 	"m": multiply,
# 	"d": divide
# }
#
# selected_option = input("""Please select one of the following options:
#
# a: add
# s: subtract
# m: multiply
# d: divide
#
# What would you like to do? """)
#
# operation = operations.get(selected_option)
#
# if operation:
# 	a = int(input("Please enter a value for a: "))
# 	b = int(input("Please enter a value for b: "))
#
# 	operation(a, b)
# else:
# 	print("Invalid selection")
#
# print()
# # Lambda expressions
#
# '''
# Lambda expressions are an alternative syntax for defining simple functions. One of the very useful features of
# lambda expressions is the fact that they are expressions, and the value they evaluate to is the function we want to create
# '''
#
# def add(a, b):
# 	return a + b
#
# # above function can replace this way.
# lambda a, b: a + b
#
# # another example
# def get_grade_average(student):
# 	return student["grade_average"]
#
# lambda student: student["grade_average"]
#
#
# print()
#
# # find max grade average marks
# students = [
# 	{"name": "Hannah", "grade_average": 83},
# 	{"name": "Charlie", "grade_average": 91},
# 	{"name": "Peter", "grade_average": 85},
# 	{"name": "Rachel", "grade_average": 79},
# 	{"name": "Lauren", "grade_average": 92}
# ]
#
# valedictorian = max(students, key=lambda student: student["grade_average"])
# print(valedictorian)
#
#
# # command-pattern implementation using lambda
#
# '''
# The only function we can't replace here is divide, because divide has a conditional statement inside.
# Lambda expressions are limited to single expressions and cannot contain statements.
# '''
# def divide(a, b):
#     if b == 0:
#         return "You can't divide by 0!"
#     else:
#         return a / b
#
#
# operations = {
#     "a": lambda a, b: a + b,
#     "s": lambda a, b: a - b,
#     "m": lambda a, b: a * b,
#     "d": divide
# }
#
# selected_option = input("""Please select one of the following options:
#
# a: add
# s: subtract
# m: multiply
# d: divide
#
# What would you like to do? """)
#
# operation = operations.get(selected_option)
#
# if operation:
#     a = int(input("Please enter a value for a: "))
#     b = int(input("Please enter a value for b: "))
#
#     print(operation(a, b))
# else:
#     print("Invalid selection")
#


# Exercise # 1
''' 
1) Use the sort method to put the following list in alphabetical order with regards to the students' names:
'''

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

sorted_list = sorted(students, key = lambda student: student["name"])
print(sorted_list)


# 2) Convert the following function to a lambda expression and assign it to a variable called exp
def exponentiate(base, exponent):
	return base ** exponent

base = 10
exponent = 2

exp = lambda base,exponent: base ** exponent

print("tradinal: ", exponentiate(10, 2))
print("lambda: ", exp)

'''
NOTE:
As we can see, instead of a normal name, we have <lambda> written instead. This is because the functions we create with lambda don't actually have names. <lambda> is really just a placeholder, because it's not a legal name in Python.
'''