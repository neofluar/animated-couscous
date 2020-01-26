import dataclasses
from datetime import datetime

__all__ = ['InitData']


@dataclasses.dataclass(frozen=True)
class InitData:

    YEAR = 2020
    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    CATEGORIES = ['Salary', 'Food', 'House', 'Car']

    @staticmethod
    def default_month() -> int:
        today = datetime.today()
        return today.month
