from settings import Settings
from user_interface import GUI
from database import DataBase


class App:

    def __init__(self):
        self.settings = Settings()
        self.gui = GUI(self.settings)
        self.database = DataBase(self.settings.DATABASE_PATH)

    def run_app(self):
        print(f'{self.settings.MONTH_NOW}')
        self.gui.start()


if __name__ == '__main__':
    App().run_app()
