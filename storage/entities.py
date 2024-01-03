from abc import ABC, abstractmethod

from mongoDB import MongoDB


class Entity(ABC):
    def __init__(self, name, entered_data):
        self.name = name
        self.entered_data = entered_data

    @abstractmethod
    def get_data(self, connection: MongoDB) -> list: pass


class Headphone(Entity):
    def __init__(self, name, entered_data):
        super().__init__(name, entered_data)

    def get_data(self, connection: MongoDB) -> list:
        collection = connection.connect_to_collection(self.name)
        data = connection.filter_model(self.entered_data, collection)
        return data


class Case(Entity):
    def __init__(self, name, entered_data):
        super().__init__(name, entered_data)

    def get_data(self, connection: MongoDB) -> list:
        collection = connection.connect_to_collection(self.name)
        data = connection.filter_diagonal(self.entered_data, collection)
        return data


class Disk(Entity):
    def __init__(self, name, entered_data):
        super().__init__(name, entered_data)

    def get_data(self, connection: MongoDB):
        collection = connection.connect_to_collection(self.name)
        data = connection.filter_volume(self.entered_data, collection)
        return data


def client_code(type_of_acc: str, **kwargs):
    if type_of_acc == 'disks':
        entity = Disk(type_of_acc.title(),
                      kwargs.get('volume'))
    elif type_of_acc == 'cases':
        entity = Case(type_of_acc.title(),
                      kwargs.get('diagonal'))
    elif type_of_acc == 'headphones':
        entity = Headphone(type_of_acc.title(),
                           kwargs.get('model'))
    else:
        return []

    return entity
