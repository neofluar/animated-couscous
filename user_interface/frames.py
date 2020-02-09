__all__ = [
    'ControlFrame',
    'InputFrame',
    'FreeFrame',
]

from abc import ABC
from tkinter import Button, Frame, Label
from tkinter import NO, NONE
from tkinter import LEFT, RIGHT, TOP, BOTTOM, SE, SW
from tkinter.messagebox import askokcancel


class BaseFrame(Frame, ABC):

    def __init__(self, root):
        super().__init__(root, height=400, width=200)
        self.pack_propagate(0)

    def pack_frame(self):
        self.pack(side=LEFT, expand=NO, fill=NONE)


class ControlFrame(BaseFrame):

    def __init__(self, root):
        super().__init__(root)
        self.config(bg='light blue')
        self.pack_frame()

        quit_button = Button(self, text='Quit', command=self.quit)  # TODO make separate class
        quit_button.pack(side=LEFT, anchor=SE)
        save_button = Button(self, text='Save', command=self.save)
        save_button.pack(side=RIGHT, anchor=SW)

    def quit(self):
        if askokcancel('Verify exit', 'Really quit?'):
            Frame.quit(self)

    def save(self):
        raise NotImplementedError('Save function not implemented yet')


class InputFrame(BaseFrame):

    def __init__(self, root):
        super().__init__(root)
        self.config(bg='light green')

        self.pack_frame()

        input_button = Button(self, text='Enter', command=self.enter_money)
        input_button.pack(side=BOTTOM)

    def enter_money(self):
        raise NotImplementedError('Enter function not implemented yet')


class FreeFrame(BaseFrame):

    def __init__(self, root):
        super().__init__(root)
        self.config(bg='pink')

        self.pack_frame()

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
