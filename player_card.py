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

import collections as col
import tkinter

from tile import Tile


class PlayerCard:
    def __init__(self, name, x0, y0):
        self.name = name
        self.card_width = 310
        self.card_height = 200
        self.points = 0
        self.minus = []
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + self.card_width
        self.y1 = self.y0 + self.card_height

        self.gray_1s = []
        self.gray_2s = []
        self.gray_3s = []
        self.gray_4s = []
        self.gray_5s = []
        self.gray = [self.gray_1s, self.gray_2s, self.gray_3s, self.gray_4s, self.gray_5s]
        self.collected_1s = []
        self.collected_2s = []
        self.collected_3s = []
        self.collected_4s = []
        self.collected_5s = []
        self.collected = [self.collected_1s, self.collected_2s, self.collected_3s, self.collected_4s, self.collected_5s]

    def create_canvas_card(self, c):
        c.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='gray')
        self.create_collected_tiles(c)
        self.create_collecting_tiles(c)

    def create_collected_tiles(self, c):
        colors = ['yellow', 'blue', 'green', 'red', 'black']
        for i in range(0, 5):
            for j in range(0, 5):
                t = Tile(colors[j])
                x = self.x0 + self.card_width/2 + (t.tile_size+t.tile_space)*j
                y = self.y0 + 5 + (t.tile_size + t.tile_space)*i
                t.update_tile_location(x, y, colors[j] + '_' + str(i) + 's')
                t.create_canvas_tile(c)
                self.collected[i].append(t)
            temp = col.deque(colors)
            temp.rotate(1)
            colors = list(temp)

    def create_collecting_tiles(self, c):
        for i in range(0, 5):
            for j in range(0, i+1):
                t = Tile('grey')
                x = self.x0 + self.card_width / 2 - (t.tile_size + t.tile_space) * (j+1)
                y = self.y0 + 5 + (t.tile_size + t.tile_space) * i
                t.update_tile_location(x, y, 'grey_' + str(j) + '_' + str(i) + 's')
                t.create_canvas_tile(c)
                self.gray[i].append(t)
