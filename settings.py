__all__ = ['Settings']

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Settings:

    YEAR = 2020
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    CATEGORIES = ('Salary', 'Food', 'House', 'Car')
    MONTH_NOW = datetime.today().month
    DATABASE_PATH = ''

