from definitions import black, blue, green, red, yellow
from space import Space


class Board():
    """5x5 Playing board to track game progress"""

    def __init__(self, name: str):
        self.game_over = False
        self.name = name
        self.spaces = [
            [Space(yellow), Space(blue), Space(green), Space(red), Space(black)],
            [Space(black), Space(yellow), Space(blue), Space(green), Space(red)],
            [Space(red), Space(black), Space(yellow), Space(blue), Space(green)],
            [Space(green), Space(red), Space(black), Space(yellow), Space(blue)],
            [Space(blue), Space(green), Space(red), Space(black), Space(yellow)],
            ]

    def check_rows(self):
        """
        Check if the end-game condition has been met. Game ends if
        any row on a Board is filled with tiles
        """
        for i in range(len(self.spaces)):
            has_tiles = [self.spaces[i][j].tile for j in range(len(self.spaces))]
            if all(has_tiles):
                self.game_over = True
        return
