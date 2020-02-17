__all__ = ['DataBase']

import os

import openpyxl


class DataBase:

    def __init__(self, path_to_db: str):
        self.path_to_db = path_to_db
        self._validate_db(self.path_to_db)
        self.workbook = self._open_last_record(self.path_to_db)
        print(self.workbook.active)

    def _validate_db(self, path: str):
        if self._no_db_folder(path):
            raise FileNotFoundError(f'No database folder at {os.path.dirname(path)}')
        if self._no_db_records(path):
            raise FileNotFoundError(f'Empty database folder at {path}')

    def _open_last_record(self, path: str) -> openpyxl.Workbook:
        last_record = self._select_last_record(path)
        workbook = self._open_record(last_record)
        return workbook

    @staticmethod
    def _no_db_folder(path: str) -> bool:
        return not os.path.exists(path)

    @staticmethod
    def _no_db_records(path: str) -> bool:
        return len(os.listdir(path)) == 0

    @staticmethod
    def _select_last_record(path: str) -> str:
        records = os.listdir(path)
        records.sort(reverse=True)
        if not records[0].endswith('.xlsx'):
            path_to_record = os.path.join(path, records[0])
            raise FileNotFoundError(
                f'Wrong record format at {path}: expected <*.xlsx>, found <{os.path.basename(path_to_record)}>')
        return os.path.join(path, records[0])

    @staticmethod
    def _open_record(record: str) -> openpyxl.Workbook:
        return openpyxl.load_workbook(record)
