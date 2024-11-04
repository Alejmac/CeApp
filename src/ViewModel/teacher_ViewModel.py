import os
import json
from Model.teacher_Model import TeacherModel

class TeacherViewModel:
    _instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TeacherViewModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.model = TeacherModel()
        self.data = self.model.get_data()
        self.teachers = self.extract_teachers()

    def extract_teachers(self):
        teachers = {}
        for materia in self.data:
            profesor = materia['profesor']
            if profesor not in teachers:
                teachers[profesor] = {
                    'correo': materia['correo'],
                    'materias': []
                }
            teachers[profesor]['materias'].append({
                'clave': materia['clave'],
                'nombre': materia['nombre'],
                'division': materia['division'],
                'grupo': materia['grupo'],
                'tipo': materia['tipo'],
                'tipo_pond': materia['tipo_pond'],
                'primer_parcial': materia['primer_parcial'],
                'segundo_parcial': materia['segundo_parcial'],
                'tercer_parcial': materia['tercer_parcial']
            })
        return teachers

    def get_teachers(self):
        return self.teachers

    def get_teacher(self, profesor):
        return self.teachers.get(profesor, {})

# Ejemplo de uso
#if __name__ == "__main__":
 #  view_model = TeacherViewModel()
 #  print("Datos de los profesores:", json.dumps(view_model.get_teachers(), indent=2, ensure_ascii=False))
   