import os
import json
from Model.data_student_Model import DataStudentModel

class DataStudentViewModel:
    _instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataStudentViewModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.model = DataStudentModel()
        self.data = self.model.get_data()

    def get_data_as_dict(self):
        return self.data

    def iterate_data(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")

# Ejemplo de uso
#if __name__ == "__main__":
 #   view_model = DataStudentViewModel()
  #  view_model.iterate_data()