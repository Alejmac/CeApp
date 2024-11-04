import flet as ft
from flet import CupertinoNavigationBar, NavigationBarDestination, icons,ElevatedButton

def create_nav_bar(page):
    nav_bar = CupertinoNavigationBar(
        bgcolor=ft.colors.BLACK,
        inactive_color=ft.colors.GREY,
       # active_color=ft.colors.RED,
        on_change=lambda e: handle_navigation(page, e.control.selected_index),
        destinations=[
            NavigationBarDestination(icon=icons.SCHEDULE, label="schedule"),
            NavigationBarDestination(icon=icons.PEOPLE, label="qualifications"),
            NavigationBarDestination(icon=icons.CALENDAR_VIEW_DAY, label="teachers"),
        ]
    )
    return nav_bar

def handle_navigation(page, index):
    routes = ["/schedule", "/qualifications", "/teachers"]
    if index < len(routes):
        page.go(routes[index])

# Exportar la función para que pueda ser importada en otros archivos
__all__ = ["create_nav_bar"]
