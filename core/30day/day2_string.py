# exercises
# Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, your age is {age}")


'''
Investigate what happens when you try to assign a value to a variable that you’ve already defined. 
Try printing the variable before and after you reuse the name.
'''
# print(f"Gender : {gender}") #you will get 'NameError'
gender = "female"


gender = "male" #it will not give any error. simply use lastest assignment
print(f"Gender: {gender} ")


#
hourly_wage = float(input("Please enter your hourly wage: "))
hours_worked = int(input("How many hours did you work this week? "))

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)
print("Your weekly income: ")
print("{:.2f}".format(hourly_wage * hours_worked))



