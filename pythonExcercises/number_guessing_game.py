# Zgadywanie numerków, user ma 7 szans, wprowadza numer, gra mówi czy jest dobry, za wysoki albo za niski, jak zgadnie to wygrywa
import random

chances = 7
# guess_number = 0
number_to_guess = random.randint(0,100)

for chance in range(0, chances): # 1 2 3 4 5 6 7 KONIEC
    user_input = int(input("Please provide number!"))

    if user_input == number_to_guess:
        print("You won")
        break
    elif user_input > number_to_guess:
        print("Number is too big")
    elif user_input < number_to_guess:
        print("Number is too low")
    else:
        print("Something is wrong")

# won = False
# while guess_number <= chances or won == True:
#     guess_number += 1
#     user_input = int(input("Please provide number!"))

#     if user_input == number_to_guess:
#         print("You won")
#         won = True
#         # break
#     elif user_input > number_to_guess:
#         print("Number is too big")
#     elif user_input < number_to_guess:
#         print("Number is too low")
#     else:
#         print("Something is wrong")

# if won:
#     print("congrats")
# else:
#     print("loser")