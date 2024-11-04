import flet as ft
from flet import Page, View, AppBar, ElevatedButton, Text, colors
from View.schedule import ScheduleView
from View.teachers_View import TeachersView
from View.qualifications_View import QualificationsView
from View.data_student_View import DataStudentView
from View.first import FirstView
from View.nav_bar_View import create_nav_bar
from View.login_View import LoginView


def main(page: Page):
    page.title = "CeApp"

    # Manejar cambios de ruta
    def route_change(route):
        page.views.clear()
        #page.appbar = create_nav_bar(page,ft)
        # Diccionario de rutas
        routes = {

            "/schedule": lambda: ScheduleView(page),
            "/teachers": lambda: TeachersView(page),
            "/qualifications": lambda: QualificationsView(page),
            "/data_student": lambda: DataStudentView(page),
            "/login": lambda: LoginView(page),
            "/first": lambda: FirstView(page)
        }
        
        view_function = routes.get(page.route, routes["/first"])
        page.views.append(view_function())  # Llama a view_function sin pasar page como argumento
 
        page.update()

    # Configurar los eventos de navegación
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)