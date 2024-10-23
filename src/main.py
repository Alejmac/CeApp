import flet as ft
from flet import app, Page

from View.first import FirstView
from View.schedule import ScheduleView
from View.qualifications_View import QualificationsView
from View.teachers_View import TeachersView
#from View.data_View import DataView  # Vista de datos
from ViewModel.nav_bar_ViewModel import NavBarViewModel
from View.nav_bar_View import create_nav_bar
from View.nav_top_View import create_nav_top
from ViewModel.login_ViewModel import LoginViewModel
from View.login_View import LoginView
from View.data_student import DataStudentView

class Main:
    def __init__(self):
        self.page = None  # Almacena la referencia a la página principal
        self.nav_view_model = NavBarViewModel(self)  # ViewModel del nav_bar

        # Inicializar vistas como None, se crearán cuando sea necesario
        #self.login_view = LoginView(self)
        self.login_view = DataStudentView(self)
        self.first_view = None
        self.schedule_view = None
        self.qualifications_view = None
        self.teachers_view = None
        self.data_view = None  # Nueva vista de datos

    def run(self, page: Page):
        """Inicializa la aplicación y muestra la vista de login."""
        self.page = page
        self.page.title = "Login Test Application"
        self.page.vertical_alignment = "start"
        self.page.horizontal_alignment = "center"
        self.page.bgcolor = "white"
        self.page.window.width = 390  # Ancho del iPhone 15
        self.page.window.height = 844  # Alto del iPhone 15

        # Construir la vista inicial (Login)
        self.login_view.build(page)
        self.set_view_visibility(self.login_view, True)

    def set_view_visibility(self, view, visible):
        """Controla la visibilidad de una vista."""
        if view is None:
            return
        for control in view.controls:
            control.visible = visible
        self.page.update()

    def handle_login_success(self):
        """Maneja el evento de login exitoso."""
        print("Login exitoso. Navegando a la vista de profesores...")
        self.set_view_visibility(self.login_view, False)
        if self.teachers_view is None:
            self.teachers_view = TeachersView(self)
            self.teachers_view.build(self.page)
        self.set_view_visibility(self.teachers_view, True)

    def show_schedule_view(self):
        """Muestra la vista de horarios."""
        self.set_view_visibility(self.teachers_view, False)
        if self.schedule_view is None:
            self.schedule_view = ScheduleView(self)
            self.schedule_view.build(self.page)
        self.set_view_visibility(self.schedule_view, True)

    def show_qualifications_view(self):
        """Muestra la vista de calificaciones."""
        self.set_view_visibility(self.teachers_view, False)
        if self.qualifications_view is None:
            self.qualifications_view = QualificationsView(self)
            self.qualifications_view.build(self.page)
        self.set_view_visibility(self.qualifications_view, True)

   # def show_data_view(self):
   #     """Muestra la vista de datos desde nav_top."""
   #     print("Navegando a la vista de datos...")
  #      if self.data_view is None:
    #        self.data_view = DataView(self)
    #        self.data_view.build(self.page)
   #     self.set_view_visibility(self.data_view, True)

# Configuración del punto de entrada
def main(page: Page):
    app_main = Main()
    app_main.run(page)

app(target=main)
