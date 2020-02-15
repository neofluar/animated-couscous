__all__ = ['GUI']

from tkinter import Tk

from settings import Settings
from .frames import ControlFrame, FreeFrame, InputFrame
from .input_corrector import InputCorrector


class GUI:

    def __init__(self, settings: Settings):
        self.settings = settings

        self.root = Tk()
        self.draw_main_window()

        self.control_frame = ControlFrame(self.root, self.settings)

        self.input_frame = InputFrame(self.root)
        self.input_corrector = InputCorrector()

        self.free_frame = FreeFrame(self.root, self.settings)

    def draw_main_window(self):
        self.root.title('MyBalance 0.1.1')
        self.root.geometry('600x400')
        self.root.resizable(0, 0)

    def start(self):
        self.root.mainloop()
