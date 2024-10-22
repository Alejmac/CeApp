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

    def run(self, page: Page):
        self.page = page
        self.page.title = "Login Test Application"
        self.page.vertical_alignment = "start"
        self.page.horizontal_alignment = "center"
        self.page.bgcolor = "white"
        self.page.window_width = 390  # Ancho del iPhone 15
        self.page.window_height = 844  # Alto del iPhone 15

        # Crear y mostrar la vista de login
        login_view = LoginView(self)
        login_view.build(page)

    def handle_login_success(self):
        print("Login exitoso. Navegando a la vista de horarios...")

# Ejemplo de uso
def main(page: Page):
    app_main = Main()
    app_main.run(page)

app(target=main)