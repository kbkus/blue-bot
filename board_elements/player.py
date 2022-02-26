from board_elements.board import Board
from board_elements.factory import Factory


class Player():
    """
    Represent a player in the game
    """

    def __init__(self, name=str):
        self.name = name
        self.factory = Factory()
        self.board = Board("player_1")
