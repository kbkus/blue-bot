import pandas as pd

from board_elements.floor import Floor


class Factory():
    """
    Board where tiles are collected by players before being moved
    to the scoring board.
    """

    def __init__(self):
        self.floor = Floor()
        self.rows = {
            "row_1": {
                "red": 1,
                "green": 1,
                "blue": 1, 
                "yellow": 1, 
                "black": 1,
            },
            "row_2": {
                "red": 2,
                "green": 2,
                "blue": 2, 
                "yellow": 2, 
                "black": 2,
            },
            "row_3": {
                "red": 3,
                "green": 3,
                "blue": 3, 
                "yellow": 3, 
                "black": 3,
            },
            "row_4": {
                "red": 4,
                "green": 4,
                "blue": 4, 
                "yellow": 4, 
                "black": 4,
            },
            "row_5": {
                "red": 5,
                "green": 5,
                "blue": 5, 
                "yellow": 5, 
                "black": 5,
            },
            "row_minus": {
                "red": 20,
                "green": 20, 
                "blue": 20, 
                "yellow": 20,
                "black": 20,
            },
        }
        self.playable_options = self.get_playable_options()

    def get_playable_options(self):
        """Convert self.rows to a pandas dataframe of all playable options"""
        options_df = pd.DataFrame(self.rows)
        options_df = options_df.reset_index()
        options_df = pd.melt(
            options_df, 
            id_vars=["index"], 
            value_vars=[x for x in options_df if x.startswith("row")]
            ).rename(columns={"index": "color", "value":"playable_spaces"})
        return options_df
