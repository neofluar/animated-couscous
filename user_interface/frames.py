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
        self.config(bg='light blue')
        self.pack_frame()

        self.settings = settings
        self._add_year_label()

        self.selected_month = StringVar(self)
        self.selected_month.set(self.settings.today_month)
        self.month_menu = OptionMenu(self, self.selected_month, *self.settings.MONTHS[1:])
        self.month_menu.config(width=12)
        self.month_menu.pack(side=TOP, pady=10)

        self.selected_category = StringVar(self)
        self.selected_category.set(self.settings.CATEGORIES[0])
        self.category_menu = OptionMenu(self, self.selected_category, *self.settings.CATEGORIES)
        self.category_menu.config(width=12)
        self.category_menu.pack(side=TOP, pady=10)

        self.quit_button = Button(self, text='Quit', command=self.quit)
        self.quit_button.pack(side=LEFT, anchor=SE)

        self.save_button = Button(self, text='Save', command=self.save)
        self.save_button.pack(side=RIGHT, anchor=SW)

    def _add_year_label(self):
        Label(self, text=self.settings.today_year).pack(side=TOP, pady=10)

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

        self.input_field = Text(self, height=20, width=20)
        self.input_field.config(bg='light green')
        self.input_field.pack(side=TOP, pady=10)

        self.input_button = Button(self, text='Enter', command=self.enter_money)
        self.input_button.pack(side=BOTTOM)

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
