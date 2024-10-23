import flet as ft
from flet import Page, Column, Text, Container
from View.nav_top_View import create_nav_top  # Importar la función create_nav_top
from ViewModel.nav_bar_ViewModel import NavBarViewModel

class TeachersView:
    def __init__(self, main_instance):
        self.main_instance = main_instance
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        page.spacing = 0
        page.padding = 0
        page.bgcolor = ft.colors.WHITE

        # Crear la barra de navegación superior
        nav_top = create_nav_top(page)

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    nav_top,  # Agregar la barra de navegación superior
                    Text("Vista de Profesores")  # Contenido principal
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            expand=True,
            margin=ft.margin.all(0),
            padding=ft.padding.all(0)
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)