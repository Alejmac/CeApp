import os
import json

class TeacherModel:
    def __init__(self):
        self.json_file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'materias_asignadas.json')
        self.data = self.load_data()

    def load_data(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_data(self):
        return self.data

# Ejemplo de uso
if __name__ == "__main__":
    model = TeacherModel()
    print("Datos del JSON:", json.dumps(model.get_data(), indent=2, ensure_ascii=False))