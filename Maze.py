from random import choice
from sys import setrecursionlimit
from time import sleep
from tkinter import *

rectangles = []
stack = []


class Rectangle(object):
    def __init__(self, width, height, number, row_count, col_count):
        self.number = number
        self.rows = row_count
        self.columns = col_count
        #            [left, right, top, bot]
        self.walls = [True, True, True, True]
        self.row = int(number/col_count)
        self.column = number % col_count
        self.width = width
        self.height = height
        self.active = False
        self.x = 0
        self.y = 0

    def draw(self, canvas, x, y, fill='white'):
        self.x = x
        self.y = y
        canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=fill, outline=fill)
        # top
        if self.walls[2]:
            canvas. create_line(x, y, x + self.width, y)
        # right
        if self.walls[1]:
            canvas.create_line(x + self.width, y, x + self.width, y + self.height)
        # bottom
        if self.walls[3]:
            canvas.create_line(x + self.height, y + self.width, x, y + self.height)
        # left
        if self.walls[0]:
            canvas.create_line(x, y + self.height, x, y)

    def move(self, list_or_rect, canvas):
        sleep(0.05)  # final
        # sleep(0.5)  # debug
        possibility = []
        # self.draw(canvas, self.x, self.y, fill='yellow')
        self.active = True
        canvas.update()
        try:
            index = self.number - 1
            if int(index / self.columns) == self.row:
                if not index < 0:
                    if not list_or_rect[index].active:
                        possibility.append(list_or_rect[index])
        except IndexError:
            pass

        try:
            index = self.number + 1
            if int(index / self.columns) == self.row:
                if not list_or_rect[index].active:
                    possibility.append(list_or_rect[index])
        except IndexError:
            pass

        try:
            index = self.number - self.rows
            if not index < 0:
                if not list_or_rect[index].active:
                    possibility.append(list_or_rect[index])
        except IndexError:
            pass

        try:
            index = self.number + self.rows
            if not list_or_rect[index].active:
                possibility.append(list_or_rect[index])
        except IndexError:
            pass

        if len(possibility) > 0:
            next_num = choice(possibility)

            # tut nujno ubrat nujniye steni
            if next_num.number - self.number == 1:
                self.walls[1] = False
                list_or_rect[next_num.number].walls[0] = False

            if next_num.number - self.number == -1:
                self.walls[0] = False
                list_or_rect[next_num.number].walls[1] = False

            if next_num.number - self.number == self.columns:
                self.walls[3] = False
                list_or_rect[next_num.number].walls[2] = False

            if next_num.number - self.number == -self.columns:
                self.walls[2] = False
                list_or_rect[next_num.number].walls[3] = False

            self.draw(canvas, self.x, self.y, fill='yellow')
            return next_num.number
        else:
            self.draw(canvas, self.x, self.y, fill='yellow')
            return -1


def gen_rects(canvas, width, height):
    canvas.update()
    rec_c = int((canvas.winfo_width()-2)/width)
    rec_r = int((canvas.winfo_height()-2)/height)
    global rectangles
    rectangles = [Rectangle(width, height, i, rec_r, rec_c) for i in range(rec_r * rec_c)]
    for row in range(rec_r):
        for col in range(rec_c):
            x = width*col+2
            y = height*row+2
            rectangles[row*rec_r+col].draw(canvas, x, y)


def run(canvas, start, stack, rectangles):
    index = start
    while index >= 0:
        stack.append(index)
        index = rectangles[index].move(rectangles, canvas)
    # print('stuck!')
    if len(stack) > 1:
        backtrack(stack, canvas, rectangles)


def backtrack(stack, canvas, rectangles):
    new_index = stack.pop()
    new_index = stack.pop()
    rectangles[new_index].draw(canvas, rectangles[new_index].x, rectangles[new_index].y, fill='magenta')
    run(canvas, new_index, stack, rectangles)


if __name__ == '__main__':
    setrecursionlimit(8000)
    master = Tk()
    canvas_width = 802
    canvas_height = 802
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)

    w.pack()
    gen_rects(w, 40, 40)
    w.update()
    run(w, 0, stack, rectangles)
    mainloop()
