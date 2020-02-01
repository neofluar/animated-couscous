__all__ = ['ControlFrame']

from tkinter import Button
from tkinter import Frame
from tkinter import NO
from tkinter import NONE
from tkinter import LEFT, BOTTOM
from tkinter.messagebox import askokcancel


class ControlFrame(Frame):

    def __init__(self, root):
        super().__init__(root, height=400, width=200)
        self.pack_propagate(0)
        self.config(bg='light blue')
        self.pack(side=LEFT, expand=NO, fill=NONE)

        # Frame buttons
        quit_button = Button(self, text='Quit', command=self.quit)  # TODO make separate class
        quit_button.pack(side=BOTTOM)
        save_button = Button(self, text='Save', command=self.save)  # TODO make separate class
        save_button.pack(side=BOTTOM)

    def quit(self):
        if askokcancel('Verify exit', 'Really quit?'):
            Frame.quit(self)

    def save(self):
        raise NotImplementedError(f'Save function not implemented yet')
