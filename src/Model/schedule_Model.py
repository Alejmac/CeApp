import os
import json

class ScheduleModel:
    def __init__(self):
        self.json_file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'schedule.json')
        self.data = self.load_data()

    def load_data(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_data(self):
        return self.data

# Ejemplo de uso
##if __name__ == "__main__":
   # model = ScheduleModel()
  #  print("Datos del JSON:", model.get_data())