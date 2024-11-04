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
        print(f"Intentando iniciar sesión con el registro {registro}   Con la contraseñas {password}")
        sesion = login_ceti(registro, password)
        if sesion:
    #Se invoca el metodo para solo iniciar sesion una vez, en lugar de hacerlo cada vez que convocamos una funcion de extraccion de datos
    #sesion = get_session(registro, password)

            materias_asignadas = get_tira_materias(sesion)
            save_file(materias_asignadas, 'aaa_tiradematerias.json')
            print(json.dumps(materias_asignadas, indent=2, ensure_ascii=False))

            calificaciones = get_grades(sesion)
            save_file(calificaciones, 'aaa_calificaiones.json')
            print(json.dumps(calificaciones, indent=2, ensure_ascii=False))

    #####Tiene problemas con la extraccion de datos, no esta jalando nada por lo menos en mi horario del juevesni el viernes#####
            horario = get_schedule(sesion)
            save_file(horario, 'aaa_horario.json') 
            print(json.dumps(horario, indent=2, ensure_ascii=False))

            student = get_student(sesion)
            save_file(student, 'aaa_estudiante.json')
            print(json.dumps(student, indent=2, ensure_ascii=False))

    # Cerrar la sesión
            sesion.close()
            #logout_ceti(sesion)
            return True
        else:
            logout_ceti(sesion)
            return False



    #def obtener_horario_servicio(self, registro, password):
    #    print("entre a obtener horario**********************")
   # #    # Realizar el login y obtener la sesión
    #    sesion = login_ceti(registro, password)
    #    if sesion is True :
    #        obtener_horario(registro, password)
    #    else:
    #        print("Error: No se pudo iniciar sesión.")
        
    
    #def obtener_calificaciones_servicio(self, registro, password):
    #    print("entre a obtener calificaciones**********************")
   #     # Realizar el login y obtener la sesión
    #    sesion = login_ceti(registro, password)
    #    
    #    if sesion is not None:
   #         # Llamar a la función para obtener las calificaciones
    #        obtener_calificaciones( registro, password)
    #        self.crear_ventana(True)  # Llamar a crear_ventana con True
    #    else:
    #        print("Error: No se pudo iniciar sesión.")
    #        self.crear_ventana(False)  # Llamar a crear_ventana con False

    #def obtener_data_servicio(self, registro, password):
        # Realizar el login y obtener la sesión
      #  print("entre a obtener data**********************")
      #  obtener_data(registro, password)
      #  sesion = login_ceti(registro, password)
        
     #   if sesion is not None:
     #       # Llamar a la función para obtener los datos
     #       obtener_data(registro, password)
      #      #self.crear_ventana(True)  # Llamar a crear_ventana con True
      #  else:
       #     print("Error: No se pudo iniciar sesión.")
      #      self.crear_ventana(False)  # Llamar a crear_ventana con False
    
 