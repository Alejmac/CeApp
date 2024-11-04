import os
from Model.qualifications_Model import cargar_calificaciones

class QualificationsViewModel:
    _instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(QualificationsViewModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.json_file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'qualifications.json')
        self.data = self.load_data()
        self.materias = []
        self.primer_parcial = []
        self.segundo_parcial = []
        self.tercer_parcial = []
        self.extract_data()

    def load_data(self):
        return cargar_calificaciones(self.json_file_path)

    def extract_data(self):
        for collection in self.data.values():
            materia = collection.get("MATERIA", "N/A")
            primer_parcial = collection.get("1ER. PARCIAL (Calf. Captura)", "N/A")
            segundo_parcial = collection.get("2DO. PARCIAL (Calf. Captura)", "N/A")
            tercer_parcial = collection.get("3ER. PARCIAL (Calf. Captura)", "N/A")
            self.materias.append(materia)
            self.primer_parcial.append(primer_parcial)
            self.segundo_parcial.append(segundo_parcial)
            self.tercer_parcial.append(tercer_parcial)

    def get_schedule(self):
        return self.data

    def get_materias(self):
        return self.materias

    def get_primer_parcial(self):
        return self.primer_parcial

    def get_segundo_parcial(self):
        return self.segundo_parcial

    def get_tercer_parcial(self):
        return self.tercer_parcial

# Ejemplo de uso
#if __name__ == "__main__":
  #  view_model = QualificationsViewModel()
  #  print("Materias:", view_model.get_materias())
  #  print("1ER. PARCIAL:", view_model.get_primer_parcial())
   # print("2DO. PARCIAL:", view_model.get_segundo_parcial())
   # print("3ER. PARCIAL:", view_model.get_tercer_parcial())