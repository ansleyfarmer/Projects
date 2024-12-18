__author__ = 'Ansley Farmer, afar@unc.edu, Onyen = afar'

from battleship import BattleshipGame

# Ask the user how many players will be playing the game.
print("*************** Welcome to BATTLESHIP! ***************")
num_of_players = 0
while num_of_players == 0:
    try:
        num_of_players = int(input("Would you like to play with 1 player or 2? "))
        if (num_of_players != 1) and (num_of_players != 2):
            raise Exception()
    except ValueError:
        print("You must enter either 1 or 2.  Please try again.")
        num_of_players = 0

# Create the new game for the correct number of players.  Then start the game!
game = BattleshipGame(num_of_players)
game.play()


