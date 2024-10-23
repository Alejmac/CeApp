import json
import os

class QualificationsViewModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(QualificationsViewModel, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.json_file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'qualifications.json')
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: El archivo {self.json_file_path} no se encontró.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: No se pudo decodificar el archivo JSON {self.json_file_path}.")
            return {}

    def get_data_as_dict(self):
        return self.data

    def get_qualifications_by_collection(self):
        collections = {}
        for collection_name, items in self.data.items():
            collections[collection_name] = items
        return collections