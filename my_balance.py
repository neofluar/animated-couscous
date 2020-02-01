from initial_data import InitData


class App:

    def __init__(self):
        self.init_data = InitData()

    def run_app(self):
        print(f'{self.init_data.YEAR}')
        print(f'{self.init_data.MONTHS}')
        print(f'{self.init_data.CATEGORIES}')
        print(f'{self.init_data.default_month()}')


if __name__ == '__main__':
    App().run_app()
