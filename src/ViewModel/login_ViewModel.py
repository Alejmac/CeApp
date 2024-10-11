from Model.login_Model import login_ceti
from Services.schedule_service import obtener_horario
from Services.qualifications_service import obtener_calificaciones

class LoginViewModel:
    def login(self, registro, password):
        # Realizar el login y obtener la sesión
        return login_ceti(registro, password)
    
    def obtener_horario_servicio(self, registro, password):
        # Realizar el login y obtener la sesión
        sesion = login_ceti(registro, password)
        
        if sesion is not None:
            # Llamar a la función para obtener el horario
            obtener_horario(sesion, registro, password)
        else:
            print("Error: No se pudo iniciar sesión.")
    
    def obtener_calificaciones_servicio(self, registro, password):
        # Realizar el login y obtener la sesión
        sesion = login_ceti(registro, password)
        
        if sesion is not None:
            # Llamar a la función para obtener las calificaciones
            obtener_calificaciones(sesion, registro, password)
        else:
            print("Error: No se pudo iniciar sesión.")
    

