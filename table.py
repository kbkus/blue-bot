import random
from typing import List

import pandas as pd

from definitions import COLORS
from player import Player
from tile import Tile


class Table():
    """ 
    Represents where left over tiles from plates go
    """
    
    def __init__(self, n_plates: int = 5, players=[Player]):
        self._players = players
        self.n_plates = n_plates
        self.bag = [Tile(color) for color in COLORS for _ in range(20)]
        self.plates = {
            "plate_1": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_2": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_3": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_4": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_5": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_leftover": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
        }
    
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

    def fill_plates(self, discard_tiles: List[Tile]):
        """
        Fill plates with tiles from bag

        :param discard: Player's discard piles from their floors
        """
        self.empty_plates()
        n_tiles = self.n_plates * 5

        # Check if there are enough plates in the bag
        if len(self.bag) >= n_tiles:
            self.deal_plates()
        # Re-fill bag with tiles from players' minus section
        else:
            self.bag.extend(discard_tiles)
            self.deal_plates()

            # Set discard piles back to being empty for each player
            for player in self.players:
                player.factory.floor.discard = []
        self._playable_options = self.get_playable_options()

    def deal_plates(self):
        """Shuffle bag and place 4 random tiles on each plate"""
        # Shuffle tiles
        plate_names = [name for name in self.plates if name[-1].isdigit()]
        random.shuffle(self.bag)
        for plate in plate_names:
            for _ in range(4):
                tile = self.bag.pop()
                self.plates[plate][tile.color] += 1


    def empty_plates(self):
        """Reset all plates to an empty state"""
        self.plates = {
            "plate_1": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_2": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_3": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_4": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_5": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
            "plate_leftover": {
                "red": 0,
                "green": 0, 
                "blue": 0, 
                "yellow": 0, 
                "black": 0, 
            },
        }
        self._playable_options = self.get_playable_options()

    @property
    def playable_options(self):
        return self._playable_options

    def get_playable_options(self):
        """Convert self.rows to a pandas dataframe of all playable options"""
        options_df = pd.DataFrame(self.plates)
        options_df = options_df.reset_index()
        options_df = pd.melt(
            options_df, 
            id_vars=["index"], 
            value_vars=[x for x in options_df if x.startswith("plate")]
            ).rename(columns={"index": "color", "value":"playable_tiles"})
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
