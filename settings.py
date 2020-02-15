__all__ = ['Settings']

import os
import calendar

from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class _Categories(Enum):
    CATEGORY0 = 0
    CATEGORY1 = 1
    CATEGORY2 = 2
    CATEGORY3 = 3
    CATEGORY4 = 4
    CATEGORY5 = 5


@dataclass(frozen=True)
class Settings:

    DATABASE_PATH = os.path.expanduser('~/app/db/')

    CATEGORIES = tuple(category.name for category in _Categories)

    YEAR = datetime.today().year
    MONTHS = tuple(calendar.month_name)

    @property
    def today_month(self) -> str:
        return self.MONTHS[datetime.today().month]

    @property
    def today_month_calendar(self) -> str:
        text_calendar = calendar.TextCalendar()
        return text_calendar.formatmonth(self.YEAR, self.MONTHS.index(self.today_month))
