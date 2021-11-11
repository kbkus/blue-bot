class Space():
    """Space on score board"""

    def __init__(self, color: str = None, minus_value: int = None):
        self.tile = None
        self.color = color
        self.minus_value = None

    @property
    def _tile(self, _tile: str):
        self.tile = _tile

    @property
    def _minus_value(self, _minus_value: int):
        self.minus_value = _minus_value