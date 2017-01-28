from sys import setrecursionlimit
from tkinter import *


class Rectangle(object):
    def __init__(self, width, height, x, y, index, canvas):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.index = index
        #            [left, right, top, bot]
        self.walls = [True, True, True, True]
        self.virgin = True

    def get_row_col(self):
        row = self.x / self.width
        col = self.y / self.height
        return row, col

    def draw(self, fill='white'):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=fill, outline=fill)
        # top
        if self.walls[2]:
            self.canvas.create_line(self.x, self.y, self.x + self.width, self.y)
        # right
        if self.walls[1]:
            self.canvas.create_line(self.x + self.width, self.y, self.x + self.width, self.y + self.height)
        # bottom
        if self.walls[3]:
            self.canvas.create_line(self.x + self.height, self.y + self.width, self.x, self.y + self.height)
        # left
        if self.walls[0]:
            self.canvas.create_line(self.x, self.y + self.height, self.x, self.y)


class MazeCreator(object):
    list_of_rects = []
    stack = []

    def __init__(self, canvas):
        self.canvas = canvas

    def gen_rects(self, width, height):
        self.canvas.update()
        cols = int((self.canvas.winfo_width() - 2) / width)
        rows = int((self.canvas.winfo_height() - 2) / height)
        for row in range(rows):
            for col in range(cols):
                self.list_of_rects.append(
                    Rectangle(width, height, width * col + 2, height * row + 2, col + row * cols, self.canvas))
                self.list_of_rects[col + row * cols].draw()


if __name__ == '__main__':
    setrecursionlimit(8000)
    master = Tk()
    canvas_width = 802
    canvas_height = 802
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack()
    maze = MazeCreator(w)
    maze.gen_rects(40, 40)
    w.update()
    mainloop()
