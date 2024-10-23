import flet as ft
from flet import app, Page

from View.first import FirstView
from View.schedule import ScheduleView
from View.qualifications_View import QualificationsView
from View.teachers_View import TeachersView
from ViewModel.nav_bar_ViewModel import NavBarViewModel
from View.nav_bar_View import create_nav_bar
from View.nav_top_View import create_nav_top
from ViewModel.login_ViewModel import LoginViewModel
from View.login_View import LoginView

class Main:
    def __init__(self):
        self.page = None  # Inicializar el atributo page
        self.login_view_model = LoginViewModel(self)  # Pasar la instancia de Main a LoginViewModel

        # Instanciar todas las vistas
        self.login_view = LoginView(self)
        self.first_view = None
        self.schedule_view = None
        self.qualifications_view = None
        self.teachers_view = None

    def run(self, page: Page):
        self.page = page
        self.page.title = "Login Test Application"
        self.page.vertical_alignment = "start"
        self.page.horizontal_alignment = "center"
        self.page.bgcolor = "white"
        self.page.window.width = 390  # Ancho del iPhone 15
        self.page.window.height = 844  # Alto del iPhone 15

        # Construir solo la vista de login inicialmente
        self.login_view.build(page)
        self.set_view_visibility(self.login_view, True)

    def set_view_visibility(self, view, visible):
        if view is None:
            return
        for control in view.controls:
            control.visible = visible
        self.page.update()

    def handle_login_success(self):
        print("Login exitoso. Navegando a la vista de horarios...")
        self.set_view_visibility(self.login_view, False)
        if self.schedule_view is None:
            self.schedule_view = ScheduleView(self)
            self.schedule_view.build(self.page)
        self.set_view_visibility(self.schedule_view, True)

    def show_teachers_view(self):
        print("Mostrando la vista de profesores...")
        self.set_view_visibility(self.login_view, False)
        if self.teachers_view is None:
            self.teachers_view = TeachersView(self)
            self.teachers_view.build(self.page)
        self.set_view_visibility(self.teachers_view, True)

# Ejemplo de uso
def main(page: Page):
    app_main = Main()
    app_main.run(page)

app(target=main)