# COPYRIGHTS AND PERMISSIONS:
# Copyright 2021 MORSECORP, Inc. All rights reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from tkinter import Canvas

from board_elements.tile import Tile


class Plate:
    def __init__(self, name: str, x0: float, y0: float, x1: float, y1:float ) -> None:
        """AI is creating summary for __init__

        Args:
            name (str): Name of plate instance
            x0 (float): Top left corner of plate
            y0 (float): Top left corner of plate
            x1 (float): Bottom right corner of plate
            y1 (float): Bottom right corner of plate
        """

        self.name = name
        self.tiles = []
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.available_colors = {"red": 0, "green": 0, "blue": 0, "yellow": 0, "black": 0}

    def add_tile(self, tile: Tile):
        """AI is creating summary for add_tile

        Args:
            tile (Tile): [description]
        """
        ind = len(self.tiles)
        if ind == 0:
            x = self.x0 + 10
            y = self.y0 + 10
        elif ind == 1:
            x = self.x0 + 40
            y = self.y0 + 10
        elif ind == 2:
            x = self.x0 + 10
            y = self.y0 + 40
        elif ind == 3:
            x = self.x0 + 40
            y = self.y0 + 40

        self.available_colors[tile.color] += 1

        tile.update_tile_location(x, y, self.name + '_' + str(ind))
        self.tiles.append(tile)

    def create_canvas_plate(self, c: Canvas):
        c.create_oval(self.x0, self.y0, self.x1, self.y1, fill='gray')
