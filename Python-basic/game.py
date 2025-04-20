import random
# computor_choice = 'scissor'
computor_choice=random.choice(['rock','paper','scissor'])
print("comp choice:" + computor_choice)
user_choice = input("what do you want rock , paper , scissor\n")
if computor_choice == user_choice:
    print("TIE")
elif user_choice == 'rock' and computor_choice == 'scissor':
    print("Win")
elif user_choice == 'paper' and computor_choice == 'scissor':
    print("Win")
elif user_choice == 'scissor' and computor_choice == 'paper':
    print("Win")
else:
    print("comp win")
