import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    ties = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3
    

        player_choice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

        if player_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)
        print("")
        print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
        print("The computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal ties

            if player == 2 and computer == 1:
                player_wins += 1
                return "You Win 😊"
            elif player == 1 and computer == 3:
                player_wins += 1
                return "You Win 😊"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You Win 😊"
            elif player == computer:
                ties += 1
                return "You tie. Play again 🤔"
            else:
                computer_wins += 1
                print("The computer wins 😢")

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame Count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nComputer Wins: " + str(computer_wins))
        print("\nTies: " + str(ties))

        print("\nPlay again?")

        while True:
            play_again = input("\n Play again? \nY for Yes or \nN for No thanks\n")
            if play_again.lower() not in ["y", "n"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\nThanks for Playing! 😁🎉✨")
            sys.exit("Bye! 🤘") 

    return play_rps 

play = rps()

play()

