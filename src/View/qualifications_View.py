import flet as ft
from flet import Page, Column, Text, ExpansionTile, Container
from View.nav_top_View import create_nav_top  # Importar la función create_nav_top
from ViewModel.nav_bar_ViewModel import NavBarViewModel

class QualificationsView:
    def __init__(self, main_instance):
        self.main_instance = main_instance
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        page.spacing = 0
        page.padding = 0
        page.bgcolor = ft.colors.WHITE

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window.width = 390
        page.window.height = 844

        # Crear la barra de navegación superior
        nav_top = create_nav_top(page)

        # Definir calificaciones (esto es solo un ejemplo, ajusta según tu lógica)
        calificaciones = {
            "Matemáticas": {"Nota": "A", "Comentarios": "Excelente"},
            "Ciencias": {"Nota": "B", "Comentarios": "Bueno"},
            "Historia": {"Nota": "C", "Comentarios": "Suficiente"}
        }

        # Crear los ExpansionTiles para cada materia
        expansion_tiles = [
            ExpansionTile(
                title=Text(f"{diccionario_nombre}", size=14, weight="bold", color=ft.colors.BLACK),
                subtitle=Text("Información adicional"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                collapsed_text_color=ft.colors.RED,
                text_color=ft.colors.RED,
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Text(f"{k}: {v}", size=12, weight="bold", color=ft.colors.BLACK)
                                for k, v in valores.items()
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            spacing=10
                        ),
                        margin=ft.margin.all(10)
                    )
                ],
                on_change=lambda e: print(f"ExpansionTile {diccionario_nombre} {'expanded' if e.data=='true' else 'collapsed'}")
            ) for diccionario_nombre, valores in calificaciones.items()
        ]

        # Crear un Column con los ExpansionTiles
        expansion_column = Column(
            controls=expansion_tiles,
            spacing=10,
            expand=True
        )

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    nav_top,  # Agregar la barra de navegación superior
                    expansion_column  # Agregar los ExpansionTiles
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            expand=True,
            margin=ft.margin.all(0),  # Sin margen alrededor del contenedor principal
            padding=ft.padding.all(0)  # Sin padding alrededor del contenedor principal
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)