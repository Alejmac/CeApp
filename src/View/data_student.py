import flet as ft
from flet import Page, Column, Text, ExpansionTile, Container
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.nav_bar_ViewModel import NavBarViewModel

class DataStudentView:
    def __init__(self, main_instance):
        self.main_instance = main_instance  # Almacenar la instancia principal
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        self.page = page
        page.spacing = 0
        page.padding = 0
        page.bgcolor = ft.colors.WHITE

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window_width = 390
        page.window_height = 844

        # Crear la barra de navegación superior
        create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)
        nav_bar.width = page.window_width  # Establecer el ancho de nav_bar

        # Definir datos del estudiante (esto es solo un ejemplo, ajusta según tu lógica)
        datos_estudiante = {
            "Nombre": "Juan Pérez",
            "Matrícula": "12345678",
            "Carrera": "Ingeniería en Sistemas",
            "Semestre": "8vo"
        }

        # Crear los ExpansionTiles para cada dato del estudiante
        expansion_tiles = [
            ExpansionTile(
                title=Text(f"{k}", size=14, weight="bold", color=ft.colors.BLACK),
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
                                for k, v in datos_estudiante.items()
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            spacing=10
                        ),
                        margin=ft.margin.all(10)
                    )
                ],
                on_change=lambda e: print(f"ExpansionTile {k} {'expanded' if e.data=='true' else 'collapsed'}")
            ) for k, v in datos_estudiante.items()
        ]

        # Crear un Column con los ExpansionTiles
        expansion_column = Column(
            controls=expansion_tiles,
            spacing=10,
            expand=True
        )

        # Crear un contenedor con margen superior de 15 px
        container = Container(
            content=expansion_column,
            margin=ft.margin.only(top=15),  # Margen superior de 15 px
            expand=True
        )

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    container,  # Agregar el contenedor con margen superior
                    nav_bar  # Agregar la barra de navegación inferior
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
        self.controls = [main_container]  # Guardar los controles para manejar la visibilidad

# Ejemplo de uso
def main(page: Page):
    view = DataStudentView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)