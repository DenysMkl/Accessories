from abc import ABC, abstractmethod

from accessories.storage.mongoDB import MongoDB

connect = MongoDB()

class Entity(ABC):
    @abstractmethod
    def __init__(self, entered_data): pass

    @abstractmethod
    def get_data(self) -> list: pass


class Headphone(Entity):
    def __init__(self, entered_data):
        self.entered_data = entered_data

    def get_data(self):
        pass


class Case(Entity):
    def __init__(self, entered_data):
        self.entered_data = entered_data

    def get_data(self):
        pass


class Disk(Entity):
    def __init__(self, entered_data):
        self.entered_data = entered_data

    def get_data(self):
        pass
