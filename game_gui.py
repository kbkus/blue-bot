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
from tkinter import *
from circle import Circle
from tile import Tile
from player_card import PlayerCard
import random


class Board:
    def __init__(self, r):
        self.num_players = 2
        self.num_circles = 5 + (self.num_players - 2)*2
        self.circles = []
        self.player_cards = []
        self.tile_colors = ['yellow', 'blue', 'green', 'red', 'black']
        self.bag = ['yellow']*20 + ['blue']*20 + ['green']*20 + ['red']*20 + ['black']*20
        random.shuffle(self.bag)
        self.recycle_bag = []

        self.c = Canvas(r, width=600, height=900, bg='saddle brown')

        self.create_and_fill_circles()
        self.create_player_cards()
        self.c.pack()

        next_turn_btn = Button(r, text='Next Turn', width=10, height=1, bg='grey', command=self.next_turn())
        next_turn_btn.place(x=50, y=800)

    def create_and_fill_circles(self):
        new_tile_colors = self.randomly_select_tiles()
        for i in range(0, self.num_circles):
            cir = Circle('C_' + str(i), 50 + (i * 100), 50, 125 + (i * 100), 125)
            cir.create_canvas_circle(self.c)
            for j in range(0, 4):
                t = Tile(new_tile_colors.pop())
                cir.add_tile(t)
                t.create_canvas_tile(self.c)
            self.circles.append(cir)

    def randomly_select_tiles(self):
        new_tiles = []
        if len(self.bag) < 4 * self.num_circles:
            self.bag += self.recycle_bag
            self.recycle_bag = []
        bag_size = len(self.bag)
        for i in range(0, 4 * self.num_circles):
            ind = random.randrange(bag_size)
            new_tiles.append(self.bag.pop(ind))
            bag_size -= 1
        return new_tiles

    def create_player_cards(self):
        for p in range(0, self.num_players):
            if p == 0:
                p_c = PlayerCard('P_' + str(p), 50, 200)
            elif p == 1:
                p_c = PlayerCard('P_' + str(p), 50, 450)
            p_c.create_canvas_card(self.c)
            self.player_cards.append(p_c)

    def next_turn(self):
        print('woot')



if __name__ == '__main__':
    root = Tk()
    root.geometry('600x900')
    b = Board(root)
    root.mainloop()