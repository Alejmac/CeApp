import flet as ft
from flet import Page, Column, Text, ExpansionTile, Container, ListView
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.quialifications_ViewModel import QualificationsViewModel  # Importar la clase QualificationsViewModel
import os

class QualificationsView:
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
        page.window.width = 390
        page.window.height = 844

        # Crear la barra de navegación superior
        create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)
        nav_bar.width = page.window.width  # Establecer el ancho de nav_bar

        # Obtener los datos de las calificaciones desde el ViewModel
        view_model = QualificationsViewModel()
        datos_calificaciones = view_model.get_qualifications_by_collection()

        # Crear los ExpansionTiles para cada colección de calificaciones
        expansion_tiles = [
            ExpansionTile(
                title=Text(f"{collection_name}", size=14, weight="bold", color=ft.colors.BLACK),
                #subtitle=Text("Información adicional"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                collapsed_text_color=ft.colors.RED,
                text_color=ft.colors.RED,
                controls=[
                    Container(
                        content=Column(
                            controls=[
                                Text(f"{k}: {v}", size=12, weight="bold", color=ft.colors.BLACK)
                                for k, v in items.items()
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            spacing=10
                        ),
                        margin=ft.margin.all(10),
                        padding=ft.padding.all(15)  # Agregar padding de 15 px
                    )
                ],
                on_change=lambda e, collection_name=collection_name: print(f"ExpansionTile {collection_name} {'expanded' if e.data=='true' else 'collapsed'}")
            ) for collection_name, items in datos_calificaciones.items()
        ]

        # Crear un ListView con los ExpansionTiles
        list_view = ListView(
            controls=expansion_tiles,
            expand=True
        )

        # Crear un contenedor con margen superior de 15 px
        container = Container(
            content=list_view,
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
    view = QualificationsView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)