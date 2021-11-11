from board import Board
from factory import Factory


class Player():
    """
    Represent a player in the game
    """

    def __init__(self, name=str):
        self.name = name
        self.factory = Factory()
        self.board = Board("player_1")
