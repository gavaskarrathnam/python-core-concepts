'''
Get the Username from the user and validate it contains '-'.
If contains ask to enter again the username.
'''

'''
username = input("Enter the username :")
while (len(username) > 0):
    if ('-' in username):
        username = input("Your username contains '-' value, Please enter the username once again :")
    else:
        print("Thanks for entry !!!")
        break
'''

'''
#Get the username (list of username) using while loop, When the username type 'End' break the loop.
'''
'''
while True:
    username = input("Enter the username :")
    if ('End'.upper() == username.upper()):
        break

    print("Entered username :" + username)
'''

'''
Get the age from the user. If age greater than 18 add to the major list otherwise add to minor list. 
'''
'''
major_list = []
minor_list = []

while True:
    age = input("Enter the user age :")

    if age.isnumeric():
        if int(age) >= 18:
            major_list.append(age)
        elif int(age) < 18:
            minor_list.append(age)
    else:
        break


print("Major list : ")
print(major_list)
print(" ")
print("Minor list : ")
print(minor_list)

'''

'''
Upto 100 get the number odd and even 
'''
'''
even_list = []
odd_list = []
for i in range(100):
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(" even value : %s " % even_list )
print(" odd value : %s " % odd_list )
'''

'''
You have list of URLs. Find the secured domain and put under the new list and remaining put on different list 
'''
'''
url_list = ['https://www.google.com', 'https://www.gmail.com', 'http://www.test.com']

secured_url = []
non_secured_url = []

for url in url_list:
    if 'https' in url:
        secured_url.append(url)
    elif 'http' in url:
        non_secured_url.append(url)
    else:
        print("NOT a valid URL : " + url)

print(" Secured URLs : %s " % secured_url)
print(" Non Secured URLs : %s " % non_secured_url)
'''

'''
# User list
'''
#username_list = ['username', 'testuser', 'no']




