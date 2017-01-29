import tkinter
from sys import exit


class BasicGUI(object):
    # initialize master window
    GUIwindow = tkinter.Tk()
    # initialize labels
    WidthLabel = tkinter.Label(GUIwindow, text='Input width of the square:')
    HeightLabel = tkinter.Label(GUIwindow, text='Input height of the square:')
    CanWidthLab = tkinter.Label(GUIwindow, text='Input width of the canvas:')
    CanHeightLab = tkinter.Label(GUIwindow, text='Input height of the canvas:')
    DelayLabel = tkinter.Label(GUIwindow, text='Input the delay of one step:')
    # initialize inputs
    WidthEntry = tkinter.Entry(GUIwindow, cursor='xterm', exportselection=0)
    HeightEntry = tkinter.Entry(GUIwindow, cursor='xterm', exportselection=0)
    CanWidthEntry = tkinter.Entry(GUIwindow, cursor='xterm', exportselection=0)
    CanHeightEntry = tkinter.Entry(GUIwindow, cursor='xterm', exportselection=0)
    DelayEntry = tkinter.Entry(GUIwindow, cursor='xterm', exportselection=0)

    def __init__(self):
        # show square's size label input pairs
        self.WidthLabel.grid(column=0, row=0)
        self.WidthEntry.grid(column=1, row=0)
        self.WidthEntry.insert(0, '40')
        self.HeightLabel.grid(column=2, row=0)
        self.HeightEntry.grid(column=3, row=0)
        self.HeightEntry.insert(0, '40')
        # show canvas' size label input pairs
        self.CanWidthLab.grid(column=0, row=1)
        self.CanWidthEntry.grid(column=1, row=1)
        self.CanWidthEntry.insert(0, '800')
        self.CanHeightLab.grid(column=2, row=1)
        self.CanHeightEntry.grid(column=3, row=1)
        self.CanHeightEntry.insert(0, '800')
        # show delay label input pairs
        self.DelayLabel.grid(column=1, row=2)
        self.DelayEntry.grid(column=2, row=2)
        self.DelayEntry.insert(0, '0.05')
        # initialize and show buttons
        self.StartButton = tkinter.Button(self.GUIwindow, text='Start!', command=self.start)
        self.QuitButton = tkinter.Button(self.GUIwindow, text='Quit!', command=self.quit)
        self.StartButton.grid(column=1, row=3)
        self.QuitButton.grid(column=2, row=3)

        self.GUIwindow.mainloop()

    @staticmethod
    def quit():
        exit()

    def start(self):
        sq_width = self.WidthEntry.get()
        sq_height = self.HeightEntry.get()
        can_width = self.CanWidthEntry.get()
        can_height = self.CanHeightEntry.get()
        print(sq_width, sq_height, can_width, can_height)
        print('this method will be overriden')


if __name__ == '__main__':
    BasicGUI()
