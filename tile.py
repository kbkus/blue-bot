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


class Tile:
    def __init__(self, color):
        self.color = color
        self.tile_size = 25
        self.tile_space = 5
        self.x0 = 0
        self.y0 = 0
        self.x1 = self.x0 + self.tile_size
        self.y1 = self.y0 + self.tile_size
        self.board_location = ''

    def update_tile_location(self, x0, y0, loc):
        self.x0 = x0
        self.y0 = y0
        self.x1 = self.x0 + self.tile_size
        self.y1 = self.y0 + self.tile_size
        self.board_location = loc

    def create_canvas_tile(self, c):
        c.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color)
