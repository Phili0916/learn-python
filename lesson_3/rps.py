import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

print("")
player_choice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

player = int(player_choice)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")

computer = int(computer_choice)
print("")
print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("The computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 2 and computer == 1:
    print("You Win 😊")
elif player == 1 and computer == 3:
    print("You Win 😊")
elif player == 3 and computer == 2:
    print("You Win 😊")
elif player == computer:
    print("You tie. Play again 🤔")
else:
    print("The computer wins 😢")


