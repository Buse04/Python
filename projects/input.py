import random 
import sys 
import argparse

class GameException(Exception):
     pass

game_count = 0

class Game:
    def __init__(self):
        self.input = input("Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")
    def choice_controller(self):
        if self.input == "1":
            print("\nYou choose 1")
        elif self.input == "2":
            print("\nYou choose 2")
        elif self.input == "3":
            print("\nYou choose 3")
        else:
            raise GameException(
                f"{args.name}, your input is invalid."
            )
    def error_controller(self):
        try:
            self.choice_controller()
        except GameException as error:
            print(f"\n{error}")
            sys.exit()
    def computer_move(self):
        self.computer = random.randint(1,3)
        print(f"\nComputer choose {self.computer}")
        if self.input > str(self.computer):
            print(f"\n{args.name}, you win")
        elif self.input == str(self.computer):
            print(f"\n{args.name}, try again to win")
        else:
            print(f"\n{args.name}, you lose")
        
        global game_count
        game_count += 1
        print("\nGame count: " + str(game_count))
        print("\nPlay again?")

        while(True):
            playagain = input("\nY for Yes or Q for Quit ")
            if playagain.lower() not in ["y" , "q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return Game()
        else:
            print(f"\nThanks for playing {args.name}")
            sys.exit()
        
    def game(self):
        try:
            #self.choice_controller()
            self.error_controller()
            self.computer_move()
        except GameException as error:
            print(f"\n{error}")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--name", metavar="name", required=True
)
args = parser.parse_args()        
player1 = Game()
player1.game()

            
            
    