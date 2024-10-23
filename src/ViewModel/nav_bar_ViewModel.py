class NavBarViewModel:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def handle_home(self):
        print("Navegando a la vista de inicio...")
        # Aquí puedes agregar la lógica para cambiar a la vista de inicio
        # Por ejemplo:
        # self.main_instance.show_home_view()

    def handle_schedule(self):
        print("Navegando a la vista de horarios...")
        # Aquí puedes agregar la lógica para cambiar a la vista de horarios
        # Por ejemplo:
        # self.main_instance.show_schedule_view()

    def handle_qualifications(self):
        print("Navegando a la vista de calificaciones...")
        # Aquí puedes agregar la lógica para cambiar a la vista de calificaciones
        # Por ejemplo:
        # self.main_instance.show_qualifications_view()

    def handle_teachers(self):
        print("Navegando a la vista de profesores...")
        # Aquí puedes agregar la lógica para cambiar a la vista de profesores
        # Por ejemplo:
        # self.main_instance.show_teachers_view()