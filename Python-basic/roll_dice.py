import random

roll = random.randint(1,6)
print(str(roll))
user_choice = int(input("guess the dice number \n"))
if user_choice == roll:
    print("correct !")
else:
    print("wrong your guess:" + str(user_choice) + "actual" + str(roll))