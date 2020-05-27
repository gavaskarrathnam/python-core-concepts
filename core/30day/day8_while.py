# # while loop
# user_number = input("Please enter a number: ")
#
# while int(user_number) < 10:
# 	print("Your number was less than 10.")
# 	user_number = input("Please select another number: ")
#
# print("Your number was at least 10.")
#
#
# # an another example;
# while True:
#     selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")
#
#     if selected_option == "a":
#         print("You selected option 'a'!")
#     elif selected_option == "b":
#         print("You selected option 'b'!")
#     elif selected_option == "c":
#         print("You selected option 'c'!")
#     elif selected_option == "q":
#         print("You selected option 'q'! Quitting the menu!")
#         break
#     else:
#         print("You selected an invalid option.")
#
#
# # continue
# for i in range(10):
#     if i%2 != 0:
#         continue
#     print(i)


# exercises
# 1
for i in "Python":
    if i == 'o':
        continue

    print(i)

# 2
target_number = 47

guess = int(input("Enter a number: "))

while guess != target_number:
    if guess > target_number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Enter a number: "))

print("You guessed correctly!")


# 3
for prm in range(100):
    if prm % 2 == 0:
        print(f"{prm} is NOT a prime number")
    else:
        print(f"{prm} is a prime number")

