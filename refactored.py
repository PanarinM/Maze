from random import choice
from time import sleep
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
        self.col = self.x / self.width
        self.row = self.y / self.height

    # def get_row_col(self):
    #     row = self.x / self.width
    #     col = self.y / self.height
    #     return row, col

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
            self.canvas.create_line(self.x + self.width, self.y + self.height, self.x, self.y + self.height)
        # left
        if self.walls[0]:
            self.canvas.create_line(self.x, self.y + self.height, self.x, self.y)

    def step(self, list_of_rect, row_c):
        sleep(0.05)
        ways = {}
        self.canvas.update()
        self.virgin = False
        try:
            if list_of_rect[self.index - 1].row == list_of_rect[self.index].row and (self.index - 1) > 0:
                if list_of_rect[self.index - 1].virgin:
                    ways.setdefault('01', list_of_rect[self.index - 1])
        except IndexError:
            pass

        try:
            if list_of_rect[self.index + 1].row == list_of_rect[self.index].row:
                if list_of_rect[self.index + 1].virgin:
                    ways.setdefault('10', list_of_rect[self.index + 1])
        except IndexError:
            pass

        try:
            if list_of_rect[self.index - row_c].col == list_of_rect[self.index].col and (self.index - row_c) > 0:
                if list_of_rect[self.index - row_c].virgin:
                    ways.setdefault('23', list_of_rect[self.index - row_c])
        except IndexError:
            pass

        try:
            if list_of_rect[self.index + row_c].col == list_of_rect[self.index].col:
                if list_of_rect[self.index + row_c].virgin:
                    ways.setdefault('32', list_of_rect[self.index + row_c])
        except IndexError:
            pass

        if len(ways) > 0:
            way = choice(list(ways.keys()))
            next_rect = ways[way]
            next_rect.walls[int(way[1])] = False
            self.walls[int(way[0])] = False
            self.draw('yellow')
            return next_rect.index
        else:
            self.draw('yellow')
            return -1


class MazeCreator(object):
    list_of_rects = []
    stack = []

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.canvas.update()
        self.cols = int((self.canvas.winfo_width() - 2) / self.width)
        self.rows = int((self.canvas.winfo_height() - 2) / self.height)

    def gen_rects(self):
        self.canvas.update()
        for row in range(self.rows):
            for col in range(self.cols):
                self.list_of_rects.append(
                    Rectangle(self.width, self.height, self.width * col + 2, self.height * row + 2,
                              col + row * self.cols, self.canvas))
                self.list_of_rects[col + row * self.cols].draw()

    def run(self, start):
        index = start
        while index >= 0:
            self.stack.append(index)
            index = self.list_of_rects[index].step(self.list_of_rects, self.cols)
        print('stuck!')
        print(self.stack)
        # TODO: Finish backtracking!
        # if len(stack) > 1:
        #     backtrack(stack, canvas, rectangles)


if __name__ == '__main__':
    # setrecursionlimit(8000)
    master = Tk()
    canvas_width = 802
    canvas_height = 802
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack()
    maze = MazeCreator(w, 40, 40)
    maze.gen_rects()
    w.update()
    maze.run(0)
    mainloop()
