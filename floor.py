from typing import List
from space import Space


class Floor():
    """
    Minus section of a player's Factory
    """

    def __init__(self):
        self.spaces = [
            Space(minus_value=1), 
            Space(minus_value=1), 
            Space(minus_value=1), 
            Space(minus_value=2),
            Space(minus_value=2),
            Space(minus_value=3),
            Space(minus_value=3),
            ]
        self._discard = []

    @property
    def discard(self):
        return self._discard

    @discard.setter
    def discard(self, val: List):
        self._discard = val
        
    def reset(self):
        """Reset Floor to original state"""
        for space in self.spaces:
            if space.tile:
                self.discard.append(space.tile)

        self.spaces = [
            Space(minus_value=1), 
            Space(minus_value=1), 
            Space(minus_value=1), 
            Space(minus_value=2),
            Space(minus_value=2),
            Space(minus_value=3),
            Space(minus_value=3),
            ]
