__all__ = ['DataBase']

import os
from typing import Tuple

import openpyxl


class DataBase:

    def __init__(self, path_to_db: str):
        self.path_to_db = path_to_db
        self.validate_path_to_db(self.path_to_db)

        self._last_record = self._select_last_record(self.path_to_db)
        self.workbook, self.sheet = self._open_record(self._last_record)

    def validate_path_to_db(self, path: str):
        if not (self._db_folder_exists(path) and self._db_records_exist(path)):
            raise FileNotFoundError(f'No database at {path}')

    @staticmethod
    def _db_folder_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def _db_records_exist(path: str) -> bool:
        return len(os.listdir(path)) != 0

    @staticmethod
    def _select_last_record(path: str) -> str:
        records = os.listdir(path)
        records.sort(reverse=True)
        return os.path.join(path, records[0])

    @staticmethod
    def _open_record(record: str) -> Tuple[openpyxl.workbook.workbook.Workbook, openpyxl.worksheet.worksheet.Worksheet]:
        workbook = openpyxl.load_workbook(record)
        sheet = workbook.active
        return workbook, sheet
