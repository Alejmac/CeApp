from Model.login_Model import login_ceti
from Services.schedule_service import obtener_horario
from Services.qualifications_service import obtener_calificaciones
from Services.student_service import obtener_data  # Importar la función obtener_data

class LoginViewModel:
    def __init__(self, main_instance):
        self.main_instance = main_instance
        self.page = None  # Inicializar el atributo page
        self.controls = [] # Referencia a la instancia de Main

    def login(self, registro, password):
        print(f"Intentando iniciar sesión con el registro {registro}...")
        print(f"Con la contraseñas {password}")
        # Realizar el login y obtener la sesión
        sesion = login_ceti(registro, password)
        if sesion:
            self.crear_ventana(True)  # Llamar a crear_ventana con True
            return True
        else:
            self.crear_ventana(False)  # Llamar a crear_ventana con False
            return False
    
    def obtener_horario_servicio(self, registro, password):
        print("entre a obtener horario**********************")
        # Realizar el login y obtener la sesión
        sesion = login_ceti(registro, password)
        if sesion is True :
            obtener_horario(registro, password)
        else:
            print("Error: No se pudo iniciar sesión.")
        
    
    def obtener_calificaciones_servicio(self, registro, password):
        print("entre a obtener calificaciones**********************")
        # Realizar el login y obtener la sesión
        sesion = login_ceti(registro, password)
        
        if sesion is not None:
            # Llamar a la función para obtener las calificaciones
            obtener_calificaciones( registro, password)
            self.crear_ventana(True)  # Llamar a crear_ventana con True
        else:
            print("Error: No se pudo iniciar sesión.")
            self.crear_ventana(False)  # Llamar a crear_ventana con False

    def obtener_data_servicio(self, registro, password):
        # Realizar el login y obtener la sesión
        print("entre a obtener data**********************")
        obtener_data(registro, password)
        sesion = login_ceti(registro, password)
        
        if sesion is not None:
            # Llamar a la función para obtener los datos
            obtener_data(registro, password)
            self.crear_ventana(True)  # Llamar a crear_ventana con True
        else:
            print("Error: No se pudo iniciar sesión.")
            self.crear_ventana(False)  # Llamar a crear_ventana con False
    
    def crear_ventana(self, estado: bool):
        if estado:
            print("Ventana creada con estado True")
            self.main_instance.handle_login_success()  # Notificar a Main sobre el éxito del login
        else:
            print("Ventana creada con estado False")