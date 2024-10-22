from Model.qualifications_Model import cargar_calificaciones

class QualificationsViewModel:
    def __init__(self):
        self.calificaciones = self.cargar_datos()

    def cargar_datos(self):
        return cargar_calificaciones()

    def obtener_calificaciones(self):
        return self.calificaciones