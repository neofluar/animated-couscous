__all__ = [
    'ControlFrame',
    'InputFrame',
    'FreeFrame',
]

from abc import ABC
from tkinter import Button, Frame, Label, OptionMenu, Text
from tkinter import StringVar
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

    def __init__(self, root, settings):
        super().__init__(root)
        self.settings = settings

        self.config(bg='light blue')
        self.pack_frame()

        year_label = Label(self, text=self.settings.today_year)
        year_label.pack(side=TOP, pady=10)

        selected_month = StringVar(self)  # TODO: one function for option menus and for buttons
        selected_month.set(self.settings.today_month)
        month_menu = OptionMenu(self, selected_month, *self.settings.MONTHS[1:])
        month_menu.config(width=12)
        month_menu.pack(side=TOP, pady=10)

        selected_category = StringVar(self)  # TODO: one function for option menus and for buttons
        selected_category.set(self.settings.CATEGORIES[0])
        category_menu = OptionMenu(self, selected_category, *self.settings.CATEGORIES)
        category_menu.config(width=12)
        category_menu.pack(side=TOP, pady=10)

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

        input_field = Text(self, height=20, width=20)
        input_field.config(bg='light green')
        input_field.pack(side=TOP, pady=10)

        input_button = Button(self, text='Enter', command=self.enter_money)
        input_button.pack(side=BOTTOM)

    def enter_money(self):
        raise NotImplementedError('Enter function not implemented yet')


class FreeFrame(BaseFrame):

    def __init__(self, root, settings):
        super().__init__(root)
        self.config(bg='pink')
        self.pack_frame()
        self.settings = settings
        self.pack_month_calendar()
        self.list_ideas()

    def pack_month_calendar(self):
        Label(self, text=self.settings.today_month_calendar, bg='pink', width=150, justify=LEFT).pack(side=TOP)

    def list_ideas(self):
        Label(self, text='\nIdeas for this frame:', bg='pink').pack(side=TOP)
        ideas = [
            '- calculator',
            '- calendar',
            '- notes',
            '- etc...',
        ]
        for idea in ideas:
            Label(self, text=idea, bg='pink').pack(side=TOP)
