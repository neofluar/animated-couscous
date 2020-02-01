from initial_data import InitData
from user_interface import GUI


class App:

    def __init__(self):
        self.init_data = InitData()
        self.gui = GUI()

    def run_app(self):
        print(f'{self.init_data.YEAR}')
        print(f'{self.init_data.MONTHS}')
        print(f'{self.init_data.CATEGORIES}')
        print(f'{self.init_data.MONTH_NOW}')

        self.gui.start()


if __name__ == '__main__':
    App().run_app()
