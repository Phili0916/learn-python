import sys
import random
import math
from enum import Enum

def rps(name='Player_1'):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    ties = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3
    

        player_choice = input(f"{name}, please enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, You must enter 1, 2, or 3")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)
        print("")
        print(f"{name} choses: {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"The computer chose: {str(RPS(computer)).replace('RPS.', '').title()}.")
        print("")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal ties

            

            if player == 2 and computer == 1:
                player_wins += 1
                return f"{name} Win\'s 😊"
            elif player == 1 and computer == 3:
                player_wins += 1
                return f"{name} Win\'s 😊"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} Win\'s 😊"
            elif player == computer:
                ties += 1
                return "You tie. Play again 🤔"
            else:
                computer_wins += 1
                print(f"The computer wins 😢 \nSorry {name} ")

        game_result = decide_winner(player, computer)
        print(game_result)


        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}: {player_wins}")
        print(f"\nComputer Wins: {computer_wins}")
        print(f"\nTies: {ties}")

        print(f"\nPlay again {name}?")

        while True:
            play_again = input(f"\n Play again {name}? \nY for Yes or \nN for No thanks\n")
            if play_again.lower() not in ["y", "n"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print(f"\nThanks for Playing {name}! 😁🎉✨")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 🤘") 
            else:
                return

    return play_rps 


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game!"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

