from Model.login_Model import * 
from Services.schedule_service import obtener_horario
from Services.qualifications_service import obtener_calificaciones
from Services.student_service import obtener_data  # Importar la función obtener_data
from Services.requests_services import *
 
class LoginViewModel:
    def __init__(self, main_instance):
        self.main_instance = main_instance
        self.page = None  # Inicializar el atributo page
        self.controls = [] # Referencia a la instancia de Main

    def login(self, registro, password):
        print(f"Intentando iniciar sesión con el registro {registro}...y Con la contraseñas {password}")
        sesion = login_ceti(registro, password)
        if sesion:
            materias_asignadas = get_tira_materias(sesion)
            save_file(materias_asignadas, 'materias_asignadas.json')
           # print("Materias asignadas guardadas:", materias_asignadas)

            calificaciones = get_grades(sesion)
            save_file(calificaciones, 'qualifications.json')
            #print("Calificaciones guardadas:", calificaciones)

            horario = get_schedule(sesion)
            save_file(horario, 'schedule.json')
            #print("Horario guardado:", horario)

            student = get_student(sesion)
            save_file(student, 'data_cleaned.json')
            #print("Datos del estudiante guardados:", student)

            logout_ceti(sesion)
            sesion.close()
            return True
        else:
            return False