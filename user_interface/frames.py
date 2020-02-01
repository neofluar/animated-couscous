__all__ = [
    'ControlFrame',
    'InputFrame',
    'FreeFrame',
]

from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import NO
from tkinter import NONE
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import TOP
from tkinter import BOTTOM
from tkinter import SE
from tkinter import SW
from tkinter.messagebox import askokcancel


class ControlFrame(Frame):  # TODO: refactor module (too much of copy-paste)

    def __init__(self, root):
        super().__init__(root, height=400, width=200)
        self.pack_propagate(0)
        self.config(bg='light blue')
        self.pack(side=LEFT, expand=NO, fill=NONE)

        # Frame buttons
        quit_button = Button(self, text='Quit', command=self.quit)  # TODO make separate class
        quit_button.pack(side=LEFT, anchor=SE)
        save_button = Button(self, text='Save', command=self.save)
        save_button.pack(side=RIGHT, anchor=SW)

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


class FreeFrame(Frame):

    def __init__(self, root):
        super().__init__(root, height=400, width=200)
        self.pack_propagate(0)
        self.config(bg='pink')
        self.pack(side=LEFT, expand=NO, fill=NONE)
        self.title_label = Label(self, text='\nIdeas for this frame:', bg='pink')
        self.title_label.pack(side=TOP)
        self.list_ideas()

    def list_ideas(self):
        ideas = [
            '- calculator',
            '- calendar',
            '- notes',
            '- etc...',
        ]
        for idea in ideas:
            Label(self, text=idea, bg='pink').pack(side=TOP)
