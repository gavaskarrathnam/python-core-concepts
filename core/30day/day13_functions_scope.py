
names = ["Mike", "Fiona", "Patrick"]
x = 53657

def add(a, b):
	print(a, b)

print(globals())

# for key, value in globals().items():
#     print("KEY {} : VALUE {} ".format(key, value))


def add(a, b):
    print(locals())
    print(a, b)

add(5, 7)

print(" ")
print(" ")
## Exercise #1
'''
1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. 
The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.
'''
print(" ----- exponentiate function ----- ")
def exponentiate(base, exponent):
    return base ** exponent

print("Exponentiate :", exponentiate(10, 2))

print("")
''' 
2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, 
and has had any excess whitespace removed.
'''
print(" ----- cleanse function ----- ")
def cleanse(word):
    return word.strip().lower()

print(" data cleanse :", cleanse("       testing data "))

print(" ")
'''
3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. 
The data should be in the following format: 
'''
data = ("Tom Hardy", "English", 42)  # name, nationality, age
# way #1
def getActors(data):
    actor = {}
    actor["name"] = data[0]
    actor["nationality"] = data[1]
    actor["age"] = data[2]
    return actor


print(getActors(data))
print(" ")
# way #2
def dictify(actor):
    name, nationality, age = actor

    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }

print(dictify(data))
print(" ")

''' 
4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. 
If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.
'''

def isPrime(num):
    status = "Yes its Prime #"

    if num < 2 or (num % 2 == 0):
        status = "No its NOT Prime #"

    return status

print("Check the No: ", isPrime(5))


### Local, Global, Build-in scope ###
var = "10"
def example():
  var = "30"
  def method():
    global var
    var = "40"
    def function():
      global var
      var = "50"
      print("Function Scope: " + var)
    function()
    print("Method Scope: " + var)
  method()
  print("Example Scope: " + var)
example()
print("Module Scope: " + var)