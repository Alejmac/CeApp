import flet as ft
from flet import app, Page

from View.first import FirstView
from View.schedule import ScheduleView
from View.qualifications_View import QualificationsView
from View.teachers_View import TeachersView
from ViewModel.nav_bar_ViewModel import NavBarViewModel
from View.nav_bar_View import create_nav_bar, handle_navigation
from View.nav_top_View import create_nav_top
from ViewModel.login_ViewModel import LoginViewModel
from View.login_View import LoginView
from View.data_student_View import DataStudentView

class Main:
    def __init__(self):
        self.page = None

    def run(self, page: Page):
        self.page = page
        self.page.spacing = 0
        self.page.padding = 0
        self.page.bgcolor = "#F1DEC6"

        # Inicializar con la vista de FirstView
        self.current_view = FirstView(self)
        self.current_view.build(page)

    def on_button_click(self, value):
        # Destruir la vista actual
        self.page.controls.clear()

        # Crear la nueva vista según el valor recibido
        if value == 1:
            self.current_view = LoginView(self)

        # Construir la nueva vista
        self.current_view.build(self.page)
        self.page.update()

# Ejemplo de uso
if __name__ == "__main__":
    ft.app(target=Main().run)