__all__ = ['ControlFrame']

from tkinter import Frame
from tkinter import Label
from tkinter import TOP


class ControlFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.pack()
        lab = Label(self, text='Hello GUI!')
        lab.pack(side=TOP)
