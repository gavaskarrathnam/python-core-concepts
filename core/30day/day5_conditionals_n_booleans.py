# boolean -> True OR False
# print(bool(0))
# print(bool(5))
#
# print(bool([]))
# print(bool(['gavaskar', 41, 'pyspark']))
#
# print(bool(""))
# print(bool("caterpiller"))
#
# print(bool(True))
# print(bool(False))
#
# print(bool("True")) # String value True
#
# name = None
# print(name)
#
#
# age = 41
# print(id(age)) # id() return, long series of numbers is an address that references a location in memory.
#
# print("A" > "a") # The ASCII code for A is 65, while a is 97
# print(5 < 10)
# print(0 == "0")                # False
# print(0 == 0)                  # True
# print(7 == 7.0)                # True
# print("Hello" == "Hello!")     # False
# print([1, 2, 3] == [1, 2, 3])  # True
#
# # case 1
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(id(a))  # 139806639351360
# print(id(b))  # 139806638418944
#
# print(a == b)  # True. Value check
# print(a is b)  # False. Mem address check
#
# # case 2
# a = [1, 2, 3]
# b = a
#
# print(id(a))  # 139685763327296
# print(id(b))  # 139685763327296
#
# print(a == b)  # True
# print(a is b)  # True

# exercise
# part #1
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print("numbers mem. address: ", id(numbers))

numbers = [1, 2, 3, 4]
numbers.append(5)

print("new_numbers address: ", id(new_numbers))
print("numbers mem. address after appended: ", id(numbers))

print(new_numbers == numbers)
print(new_numbers is numbers)

# part 2
input_value = float(input("Enter the input value: "))

if input_value > 0 or input_value > 0.0:
    print(f"{input_value} is positive")
elif input_value < 0 or input_value < 0.0:
    print(f"{input_value} is negative")
else:
    print(f"{input_value} is zero")

# part 3
employee_name = input("Please Employee Name: ").strip().title()
hourly_wage = float(input(f"Please enter {employee_name}'s hourly wage: "))
work_hours = float(input(f"Please enter {employee_name} work hours this week: "))

if work_hours > 40:
    overtime_hr = work_hours - 40
    regular_wage = 40 * hourly_wage
    overtime_wage = float((hourly_wage * 110)/100) * overtime_hr # overtime hr wage is 110%
    week_net_income = "{:.2f}".format((regular_wage + overtime_wage))
else:
    week_net_income = "{:.2f}".format(hourly_wage * work_hours)

print(f"{employee_name} earned ${week_net_income} this week")
