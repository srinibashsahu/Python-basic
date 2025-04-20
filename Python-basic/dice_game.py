import random

def roll_dice():
    dice_total=random.randint(1,6)+random.randint(1,6)
    return dice_total
def main():
    player1=input("Enter Player1 name\n")
    player2=input("Enter Player2 name\n")

    roll1=roll_dice()
    roll2=roll_dice()

    if roll1>roll2:
        print("Player1 Win")
        print("Player1 total: ",roll1,'player2 total: ',roll2)
    elif roll1== roll2:
        print("TIE")
        print("Player1 total: ",roll1,'player2 total: ',roll2)
    else:
        print("Player2 Win")
        print("Player1 total: ",roll1,'player2 total: ',roll2)
main()