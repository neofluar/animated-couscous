__all__ = ['DataBase']

from dataclasses import dataclass


@dataclass()
class DataBase:
    path: str
