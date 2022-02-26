import random
from typing import List
from pprint import pprint

import pandas as pd
from tkinter import *

from definitions import COLORS
from board_elements.player import Player
from board_elements.tile import Tile
from board_elements.plate import Plate


class Table:
    """ 
    Represents where left over tiles from plates go
    """
    
    def __init__(self, players: List[Player], root = None, n_plates: int = 5):
        self._players = players
        self.n_plates = n_plates
        self._bag = [Tile(color) for color in COLORS for _ in range(20)]
        self.plates = []
        for i in range(0, self.n_plates):
            self.plates.append(Plate('plate_' + str(i), 50 + (i * 100), 50, 125 + (i * 100), 125))
        self.c = None
        if root:
            self.c = Canvas(root, width=600, height=900, bg='saddle brown')
            

    @property
    def bag(self):
        return self._bag

    @bag.setter
    def bag(self, updated_bag: List[Tile]):
        self._bag = updated_bag

    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, updated_players: List[Player]):
        self._players = updated_players

    @staticmethod
    def get_discard_tiles(players):
        """Combine discard tiles from all players"""
        discard_tiles = []
        for player in players:
            discard_tiles.extend(player.factory.floor.discard)

    def fill_plates(self):
        """
        Fill plates with tiles from bag
        """
        self.empty_plates()
        n_tiles = self.n_plates * 5

        # Check if there are enough plates in the bag
        if len(self.bag) >= n_tiles:
            self.deal_plates()

        # Re-fill bag with tiles from players' minus section
        else:
            # Set discard piles back to being empty for each player
            for player in self.players:
                # Add player's discard pile to list of discard_tiles
                self.bag.extend(player.factory.floor.discard)
                # Set player's discard back to empty
                player.factory.floor.discard = []
            # Deal plates
            self.deal_plates()
        self._playable_options = self.get_playable_options()

    def deal_plates(self):
        """Shuffle bag and place 4 random tiles on each plate"""
        # Shuffle tiles
        # Get list of string plate names. Plate names end in a digit
        plate_names = [plate.name for plate in self.plates if plate.name[-1].isdigit()]
        random.shuffle(self.bag)
        for plate in self.plates:
            if plate.name[-1].isdigit():
                # If a canvas has been created, add plate to GUI
                if self.c:
                    plate.create_canvas_plate(self.c)

                # Add tiles in range to each plate
                for i in range(4):
                    tile = self.bag.pop()
                    plate.add_tile(tile)
                    if self.c:
                        tile.create_canvas_tile(self.c)
                        self.c.pack()

    def empty_plates(self):
        """Reset all plates to an empty state"""
        # for plate in self.plates:
        #     del plate
        self.plates = []
        for i in range(0, self.n_plates):
            self.plates.append(Plate('plate_' + str(i), 50 + (i * 100), 50, 125 + (i * 100), 125))

        self._playable_options = self.get_playable_options()

    @property
    def playable_options(self):
        return self._playable_options

    def get_plates_dict(self):
        plates_dict = {plate.name: plate.available_colors for plate in self.plates}
        return plates_dict

    def get_playable_options(self):
        """Convert self.rows to a pandas dataframe of all playable options"""
        options_df = pd.DataFrame(self.get_plates_dict())
        options_df = options_df.reset_index()
        options_df = pd.melt(
            options_df, 
            id_vars=["index"], 
            value_vars=[x for x in options_df if x.startswith("plate")]
            ).rename(columns={"index": "color", "value": "playable_tiles"})
        self._playable_options = options_df
        return self._playable_options

    def game_state(self, print=False):
        """Log current game state"""
        player_1 = self.players[0]
        player_2 = self.players[1]
        if print:
            print(f"Current players: {len(self.players)}")
            print(f"Player_1 factory: {player_1.factory.playable_options}")
            print(f"Player_2 factory: {player_2.factory.playable_options}")
            print()
            print(f"Player_1 discard: {player_1.factory.floor.discard}")
            print(f"Player_2 discard: {player_2.factory.floor.discard}")
            print()
            print(f"Current plate setup:")
            for plate in self.plates:
                print(f"{plate}: {self.plates[plate].items()}")
            print()
        path = "log_game_state"
        player_1.factory.playable_options.to_csv(f"{path}/player_1_playable_options.csv")
        player_2.factory.playable_options.to_csv(f"{path}/player_2_playable_options.csv")
        self.playable_options.where(self.playable_options["playable_tiles"] != 0).dropna().to_csv(f"{path}/table_playable_options.csv")
