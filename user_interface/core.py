__all__ = ['GUI']

from tkinter import Tk

from .frames import ControlFrame, FreeFrame, InputFrame
from settings import Settings


class GUI:

    def __init__(self, settings: Settings):
        self.settings = settings

        # Main window settings
        self.root = Tk()
        self.root.title('MyBalance 0.1.1')
        self.root.geometry('600x400')
        self.root.resizable(0, 0)

        # Frames
        self.control_frame = ControlFrame(self.root)
        self.input_frame = InputFrame(self.root)
        self.free_frame = FreeFrame(self.root)

    def start(self):
        self.root.mainloop()
