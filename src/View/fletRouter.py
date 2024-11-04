import flet as ft
from flet import Page, Column
from View.schedule import ScheduleView
from View.teachers_View import TeachersView
from View.qualifications_View import QualificationsView
from View.data_student_View import DataStudentView
from View.login_View import LoginView
from View.first import FirstView

class Router:
    def __init__(self, page):
        self.page = page
        self.routes = {
            "/schedule": lambda: ScheduleView(page),
            "/teachers": lambda: TeachersView(page),
            "/qualifications":lambda: QualificationsView(page),
            "/data_student": lambda: DataStudentView(page),
            "/login": lambda: LoginView(page),
            "/first": lambda: FirstView(page)
        }

    def route_change(self, e: ft.RouteChangeEvent):
        self.page.views.clear()
        self.page.views.append(
            self.routes[e.route](self.page)
        )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)