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
from random import randrange
import numpy as np


def create_tile_grid_coords(x_start: int, y_start: int, tile_size: int, tile_space: int, n_x: int, n_y:int):
    """
    function output grid coordinates for n_x X n_y grid of tiles

    :param x_start: top left tile in grid's top left x-coordinate
    :param y_start: top left tile in grid's top left y-coordinate
    :param tile_size: length of side of tile
    :param tile_space: small empty space left between tiles
    :param n_x: number rows of tiles
    :param n_y: number columns of tiles
    :return: numpy of n_x X n_y sizd where each element stores the x0, y0, x1, y1 coordinates for tile
    """
    grid_coordinates = np.zeros([n_x, n_y])
    for i in range(0, n_x):
        for j in range(0, n_y):
            x = x_start + (i * (tile_size + tile_space))
            y = y_start + (i * (tile_size + tile_space))
            grid_coordinates[i, j] = {'x0':x, 'y0':y, 'x1':x + tile_size, 'y1':y + tile_size}
    return grid_coordinates

tile_colors = ['yellow', 'blue', 'green', 'red', 'black']
tile_size = 25

root = Tk()
root.geometry('600x900')

c = Canvas(root, width=600, height=900, bg='saddle brown')
player_card_coords = create_tile_grid_coords(50, 200, 300, 25, 2, 1)
player1_card = c.create_rectangle(
    player_card_coords[0][0]['x0'],
    player_card_coords[0][0]['y0'],
    player_card_coords[0][0]['x1'],
    player_card_coords[0][0]['y1'],
    fill='grey')
player1_card = c.create_rectangle(
    player_card_coords[1][0]['x0'],
    player_card_coords[1][0]['y0'],
    player_card_coords[1][0]['x1'],
    player_card_coords[1][0]['y1'],
    fill='grey')
c_ind = 0
cir = []
tiles = []
board = np.zeros([5, 5])
x0 = [60, 60, 90, 90]
x1 = [x + tile_size for x in x0]
print(x1)
y0 = [60, 90, 60, 90]
y1 = [y + tile_size for y in y0]
print(y1)
for i in range(0, 5):
    # top circles
    cir.append(c.create_oval(50 + (i*100), 50, 125 + (i*100), 125, fill='grey'))

    # tiles in circles
    tiles.append(c.create_rectangle(x0[0] + (i*100), y0[0], x1[0] + (i*100), y1[0], fill=tile_colors[randrange(5)]))
    tiles.append(c.create_rectangle(x0[1] + (i*100), y0[1], x1[1] + (i*100), y1[1], fill=tile_colors[randrange(5)]))
    tiles.append(c.create_rectangle(x0[2] + (i*100), y0[2], x1[2] + (i*100), y1[2], fill=tile_colors[randrange(5)]))
    tiles.append(c.create_rectangle(x0[3] + (i*100), y0[3], x1[3] + (i*100), y1[3], fill=tile_colors[randrange(5)]))

    # colored board
    for j in range(5):
        c_ind += j
        c_ind %= 5
        board[i][j] = c.create_rectangle(
            200 + (j*tile_size+5),
            200 + (i*tile_size+5),
            230 + (j*tile_size),
            230 + (i*tile_size),
            fill=tile_colors[c_ind],
            stipple='gray75'
        )
        c_ind +=1


test = c.create_rectangle(100, 350, 125, 375, fill='grey')

c.pack()

root.mainloop()