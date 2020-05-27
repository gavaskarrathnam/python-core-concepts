# # Join
# name_list = ["gavaskar", "rathnam"]
# #name_list = ", ".join(name_list)
# #print(f"List of names are {name_list}")
# print(f"List of names are {','.join(name_list)}")
#
#
# # split
# user_numbers = input("Please enter 5 numbers seprated by comma: ")
# tupe_no = tuple(user_numbers.split(","))
# list_no = user_numbers.split(",")
# print(tupe_no)
# print(list_no)
#
# cleansed_list = []
# for no in list_no:
#     cleansed_list.append(no.strip())
#
# print(f" Cleansed list: {cleansed_list}")
# print(list("gavaskar rathnam"))
#
# # list length
# print(f"list length : {len(cleansed_list)}")
#
# # new line
# print("Super Special Mega Awesome Program\n\nBy Phillip Best")
#
#
# # slice
#
# #For example, [start_at_index:stop_at_index:move_in_steps_of].
#
# name = "gavaskar"
# print(name[0:5])
# print(name[5])
# print(name[3:-1])
# print(name[:3])
# print(name[:-3])
#
#
# t = (1, 2, 3, 4, 5)
# print(t[4:1]) # ()
# print(t[4:2]) # ()
# print(t[4:2:-1] ) # (5, 4)


# exercises

'''
1) Ask the user to enter their given name and surname in response to a single prompt.
Use split to extract the names, and then assign each name to a different variable.
For this exercise, you can assume that the user has a single given name and a single surname.
'''
# name = input("Please enter your full name:")
# name = name.split(" ")
# print(f"First name: {name[0].strip().title()}")
# print(f"last name: {name[1].strip().title()}")


'''
2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. 
Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
'''
number = "1 | 2 | 3 | 4 | 5"
number_list = number.split(" | ")
cleansed_no_list = []
for no in number_list:
    cleansed_no_list.append(int(no.strip()))

print(cleansed_no_list)
print(" ")

'''
3)
'''
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
print(" --- QUOTES ---")
for quote in quotes:
    print(quote[1:-1])

print(" ")

'''
4) word length
'''
line = input("Please enter the string: ")
print("total no. of charactors :", len(line))
print("word count: ", len(line.split(" ")))