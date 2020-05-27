
username_list = ["user1", "user2", "user3"]
default_pwd = input("Enter the password :")

mydictionary = {}

for i in username_list:
    mydictionary[i] = default_pwd

print(mydictionary)

print("-------------------")

contactlist = {'gr':'999-999-9999', 'tg':'555-555-5555'}
contactlist.has_key("tg")

callingno = input("Calling mobile number :")
for key, value in contactlist.items():
    if callingno in value:
        print (' calling user ' + key)




list1 = ["user1", "user2", "user3"]
list2 = ["user1", "user2", "user3", "user4"]

comb_list = list1
for i in list2:
    comb_list.append(i)

print(comb_list)

newuserset = {}
newuserset = set(comb_list)

print(list(newuserset))

