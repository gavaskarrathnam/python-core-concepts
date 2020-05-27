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
#
# for movie in movies:
#     print(f"'{movie[0]}' released on '{movie[2]}' directed by '{movie[1]}'")
#
#
# for rng in range(3, 12, 3):
#     print(f"{rng},")
#
# # reverse order
# print("reverse order :")
# for rng1 in range(10, 0, -1):
#     print(f"{rng1},")
#
#
# print(list(range(0, 10)))

# exercises
'''
1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop:
their name, the number of hours worked last week, and their hourly rate.
Print how much each employee is due to be paid at the end of the week in a nice, readable format.
'''
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]


average_wage = 0.0
total_wage = 0.0

for emp in employees:
    print("******************************")
    print(f"    {emp[0]} Detail:")
    print("******************************")
    print(f"hrs worked in last week: {emp[1]}")
    print(f"hourly rate : {emp[2]}")
    print(f"last week net payment: {(emp[1] * emp[2]):.2f}")
    total_wage += emp[2]
    print("--------------------------------")

print(f"total_wage: {total_wage}")

# 2) For the employees above, print out those who are earning an hourly wage above average.
average_wage = total_wage / len(employees)
print(f"Total no. of employees: {len(employees)}")
print(f"Average wage is: {average_wage}")

for l_emp in employees:
    if(l_emp[2] > average_wage):
        print(f"{l_emp[0]} wage is above average")
