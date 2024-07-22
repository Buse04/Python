import argparse
import sys
import random 

class Gameexception(Exception):
    pass

parser =  argparse.ArgumentParser()
parser.add_argument(
    "--name", metavar="name", required=True
)
args = parser.parse_args()

game_count= 0
wins = 0

class Game:
    def __init__(self):
        self.input = input(f"\n{args.name}, guess which number I am thinking of: 1, 2 or 3 ==> ")
    def player_controller(self):
        if self.input == "1" or self.input == "2" or self.input == "3":
            print(f"\n{args.name}, you chose {self.input}.")
        else:
            raise Gameexception(
                f"{args.name}, your input is invalid."
            )
    def error_controller(self):
        try:
            self.player_controller()
        except Gameexception as error:
            print(f"\n{error}")
            sys.exit()
    def computer_move(self):
        self.error_controller()
        self.computer = random.randint(1,3)
        print(f"\nI chose {self.computer}")
        if self.input == str(self.computer):
            print(f"\n{args.name}, you win")
        else:
            print(f"\n{args.name}, you lose")
        global wins 
        wins += 1
        print(f"\nYou have {wins} wins.")
        global game_count 
        game_count += 1
        if game_count == 1:
            print(f"\nYou played {game_count} time.")
        elif game_count > 1:
            print(f"\nYou played {game_count} times.")
        print(f"\nYour win percentage is {game_count / wins:.2%}")
    def game(self):
        try:
            self.error_controller()
            self.computer_move()
        except Gameexception as error:
            print(f"\n{error}")


player = Game()
player.game()


