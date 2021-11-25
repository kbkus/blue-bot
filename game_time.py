# Install dependencies
import itertools
import random
from pprint import pprint
import pandas as pd
from tkinter import *

from definitions import COLORS
from player import Player
from table import Table

# Display all rows in dataframes
pd.set_option('display.max_rows', None)

# Set up game with 2 players
player_1 = Player("Kaci")
player_2 = Player("Avi")

# Create table with 5 plates, and assign the players
root = Tk()
root.geometry('600x900')
table = Table(n_plates=5, root=root, players=[player_1, player_2])


# Fill table
table.fill_plates()

print("Current table plates:")
pprint(table.get_plates_dict())
print()
#
# Playable options of plates on table
table_options = table.playable_options
table_options = table_options.where(table_options["playable_tiles"] != 0).dropna()
print("Table options")
print(table_options)

#
# # Playable options of player factories
# player_options = player_1.factory.playable_options
# player_options = player_options.where(player_options["playable_spaces"] != 0).dropna()
#
# table.game_state()
#
# # Get all possible options
# all_options = []
# for color in COLORS:
#     player_condition = (player_options["color"] == color) & (player_options["playable_spaces"] > 0)
#     table_condition = (table_options["color"] == color) & (table_options["playable_tiles"] > 0)
#     color_options = itertools.product(player_options.loc[player_condition].index.values, table_options.loc[table_condition].index.values)
#     all_options.extend(list(color_options))
#
# print(all_options)
#
# # Select one option
# random.choice(all_options)

root.mainloop()