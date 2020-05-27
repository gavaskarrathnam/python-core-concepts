
#username = input("Enter username :")
user_list = ['username1', 'user2', 'user3']
#pwd_list = ['pwd1', 'pwd2', 'pwd3']
email_list = ['usera1@gmail.com', 'user2@gmail.com', 'user3@gmail.com']

'''
user_pwd_list = user_list
for i in pwd_list:
    user_pwd_list.append(i)

print(user_pwd_list)
print(" -------------- ")
'''

print ("user list: %s" % (user_list))
print ("email list: %s" % (email_list))

user_email_list = []
for i in user_list:
    user_email_list.append(i)
    
for j in email_list:
    user_email_list.append(j) 
         
for i in user_email_list:
    if len(i) <= 7:
        print("your  item length less than 7 >>> item value :" + i) 
    if '@' not in i:
        print("User name alone :" + i)
        if len(i) > 7:
            print("your user name should not more than 7 char ---> " + i)
    else:
        print("your item :" + i)

print ("user_email_list: %s" % (user_email_list))
del user_email_list[len(user_email_list)-2]
print ("final user_email_list: %s" % (user_email_list)) 


 




 
