email = input("Enter the email :")
if '@' in email and len(email) < 7:
    print ("Valid email with lenght with in 7")
elif '@' in email and len(email) > 7:
    print ("Valid email but lenght not with in 7")
else:
    print ("Not valid")