print(4 + 5)
print(4 - 11.5)
print(-4 - 9)
print(8 * 8)
print(2 * 25.5)
print("{:.2f}".format(8.2 * 34))

#exerises

#Print your age to the console.
#Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
age = int(input("enter your age: "))

no_of_days = (age * 365)
no_of_weeks = (age * 52)
no_of_months = (age * 12)
#no_of_weeks = (no_of_days / 7)  # this case, may chance result get wrong because get float value
#no_of_months = (no_of_weeks / 4) # this case, may chance result get wrong because some month have 5 weeks

print(f"living number of days: {no_of_days}")
print(f"living number of weeks: {no_of_weeks}")
print(f"living number of months: {no_of_months}")


#Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
pi = 3.141
radius = 5

#area_of_circle = (pi * (radius * radius))
#area_of_circle = (pi * radius ** 2) #  ** is square a number
area_of_circle = (pi * pow(radius, 2)) # pow -> first param base no. and second param value is the exponent

#print("Area of circle with a radius of 5 units {:.2f}".format(area_of_circle))
print(f"Area of circle with a radius of 5 units : {area_of_circle}")
