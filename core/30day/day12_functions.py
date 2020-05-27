# first 10 even numbers

def get_even_number(num):
    print("first 10 even no: ")
    for n in range(2, (num + 1), 2):
        print(n)

get_even_number(20)


print(" ")

print(" ")
def x_print(requested_output, quantity):
	for i in range(quantity):
		print(requested_output)


x_print(requested_output="Hello", quantity=5)

print(" ")
print(" --------------------------------------------------------")
print(" ")

def add(param1, param2):
    if type(param1) != int or type(param2) != int:
        print("Your one of parameter not valid type. Hit: It should be interger")
        
    if(param1 < 0 or param2 <= 0):
        print("Please enter valid number")
        
    return (param1 + param2)


def add(param1, param2):
    if type(param1) != int or type(param2) != int:
        print("Your one of parameter not valid type. Hit: It should be interger")

    if (param1 <= 0 or param2 <= 0):
        print("Please enter valid number")

    return (param1 + param2)


def multi(param1, param2):
    if type(param1) != int or type(param2) != int:
        print("Your one of parameter not valid type. Hit: It should be interger")

    if (param1 <= 0 or param2 <= 0):
        print("Please enter valid number")

    return (param1 * param2)


def div(param1, param2):
    if type(param1) != int or type(param2) != int:
        print("Your one of parameter not valid type. Hit: It should be interger")

    if (param1 <= 0 or param2 <= 0):
        print("Please enter valid number")

    return (param1 // param2)


def sub(param1, param2):
    if type(param1) != int or type(param2) != int:
        print("Your one of parameter not valid type. Hit: It should be interger")

    if (param1 <= 0 or param2 <= 0):
        print("Please enter valid number")

    return (param1 - param2)


print("Addition :", add(10, 10))
print("Multiplication :", multi(10, 10))
print("Division :", div(10, 10))
print("Substraction :", sub(10, 10))

print(" ")
print(" ")
## exercise # 2
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

# output like:  Breaking Bad (2008) - 5 seasons
def print_show_info(tv_shows):
    for tv_show in tv_shows:
        print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} season(s)")

series_data = [
	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

#print_show_info(tv_show)
print_show_info(series_data)

print(" ")
print(" ")


def is_palindrome(word):
    word = word.strip().lower()
    reverse = word[::-1]

    print("Gavaskar Rathnam".casefold()) # removes all the cases and return lower

    name = ["g", "a", "v", "a", "s", "k", "a", "r"]
    print("list reverse : ", name.reverse())

    print("actual word :", word)
    print("revese :", reverse)
    if(word == reverse):
        print("Yes, given word Palindrome")
    else:
        print("No, given word NOT Palindrome")

is_palindrome("Idappadi ")