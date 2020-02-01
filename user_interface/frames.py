__all__ = [
    'ControlFrame',
    'InputFrame',
]

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
        save_button = Button(self, text='Save', command=self.save)
        save_button.pack(side=BOTTOM)

    def quit(self):
        if askokcancel('Verify exit', 'Really quit?'):
            Frame.quit(self)

    def save(self):
        raise NotImplementedError('Save function not implemented yet')


class InputFrame(Frame):

    def __init__(self, root):
        super().__init__(root, height=400, width=200)
        self.pack_propagate(0)
        self.config(bg='light green')
        self.pack(side=LEFT, expand=NO, fill=NONE)

        # Frame buttons
        input_button = Button(self, text='Enter', command=self.enter_money)
        input_button.pack(side=BOTTOM)

    def enter_money(self):
        raise NotImplementedError('Enter function not implemented yet')
