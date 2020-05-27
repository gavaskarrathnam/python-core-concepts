

#

vegetables_list = ["carrot", "lettuce", "broccoli", "onion", "carrot"]

vegetables_tuple = ("carrot", "lettuce", "broccoli", "onion", "carrot")

# Set is not reliably ordered. contains only unique elements
vegetables_set = {"carrot", "lettuce", "broccoli", "onion", "carrot"}


#list iteration/unpacking
print(" --- LIST --- ")
for ls in vegetables_list:
    print(ls)

print(" ")
#tuple iteration/unpacking
print(" --- TUPLE --- ")
for tp in vegetables_tuple:
    print(tp)

print(" ")
#set iteration/unpacking [ Set is not reliably ordered. contains only unique elements ]
print(" --- SET --- ")
for st in vegetables_set:
    print(st)


print(" ")


# Create your dictionary class
class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

    # Main Function


dict_obj = my_dictionary()
name_age_dic = my_dictionary()
for i in range(10):
    name_age_dic.add(i, "data "+ str(i))

print(" --- DICTIONARY --- ")
for key, value in name_age_dic.items():
    print("KEY {} : VALUE {} ".format(key, value))


print(" ----- ***** ----- ***** ----- ***** ")

print(" --- SET OPERATIONS --- ")

vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.add("potato")
vegetables.add("sweet potato")
print(vegetables)


vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin", 'tomato'])
print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}

print(" after delete the element ")
vegetables.remove("lettuce")
print(vegetables)

print(" after discard the element ")
vegetables.discard("sweet potato")
print(vegetables)
''' 
If we try to remove an item which doesn't exist, we get a KeyError. If we don't want this KeyError to be raised, we can use another method called discard.

discard works in exactly the same way, but it will only try to remove the item if it exists. If the item isn't in the set, the operation does nothing.

Both remove and discard require us to know what we want to remove, but sometimes it doesn't really matter. We just want one of the items. In these cases we should use the pop method.
'''


print("### Exercise # 1 ###")
print(" ")
print("New set initialzation")

s = set()
s.add("gavaskar")
s.add("ramya")

print(s)

print("set update")
s.update(["krishnaraghav", "tannave gavaskar"])

print(s)


print(" ")
s = set()
s.update(range(1, 4))

random_values = {"r", 1, ("Python", "C", "Rust")}

print(s.union(random_values))
print(s.symmetric_difference(random_values))
print(s.intersection(random_values))


print(" ")
numbers = range(27, 54)
user_number = int(input("Enter a number: "))

if user_number in numbers:
	print("Your number is in the valid range.")
else:
	if user_number < numbers[0]:
		print("Your number is too low.")
	else:
		print("Your number is too high.")