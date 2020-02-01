__all__ = ['GUI']

from tkinter import Tk
from .frames import ControlFrame


class GUI:

    def __init__(self):
        self.root = Tk()
        self.control_frame = ControlFrame(self.root)

    def start(self):
        self.root.mainloop()
