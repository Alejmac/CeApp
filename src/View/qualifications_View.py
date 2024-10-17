import flet as ft
from flet import Page, Column, Text, ExpansionTile, Container
from nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from nav_top_View import create_nav_top  # Importar la función create_nav_top

def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0
    page.bgcolor = ft.colors.WHITE  # Línea donde se cambia el fondo a blanco

    # Ajustar el tamaño de la ventana a la resolución del iPhone 15
    page.window_width = 390
    page.window_height = 844

    # Crear la barra de navegación superior
    nav_top = create_nav_top(page)

    # Crear los ExpansionTiles para cada materia
    expansion_tiles = [
        ExpansionTile(
            title=Text(f"Materia {i+1}", size=14, weight="bold", color=ft.colors.BLACK),
            subtitle=Text("Información adicional"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            collapsed_text_color=ft.colors.RED,
            text_color=ft.colors.RED,
            controls=[
                Container(
                    content=Column(
                        controls=[
                            Text("Parcial 1", size=12, weight="bold", color=ft.colors.BLACK),
                            Container(
                                content=Text("p1: Calificación", text_align="center"),
                                width=100,
                                height=50,
                                bgcolor=ft.colors.GREY_200,
                                alignment=ft.alignment.center,
                                border=ft.border.all(1, ft.colors.WHITE)
                            ),
                            Text("Parcial 2", size=12, weight="bold", color=ft.colors.BLACK),
                            Container(
                                content=Text("p2: Calificación", text_align="center"),
                                width=100,
                                height=50,
                                bgcolor=ft.colors.GREY_200,
                                alignment=ft.alignment.center,
                                border=ft.border.all(1, ft.colors.WHITE)
                            ),
                            Text("Parcial 3", size=12, weight="bold", color=ft.colors.BLACK),
                            Container(
                                content=Text("p3: Calificación", text_align="center"),
                                width=100,
                                height=50,
                                bgcolor=ft.colors.GREY_200,
                                alignment=ft.alignment.center,
                                border=ft.border.all(1, ft.colors.WHITE)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10
                    ),
                    margin=ft.margin.all(10)
                )
            ],
            on_change=lambda e: print(f"ExpansionTile {i+1} {'expanded' if e.data=='true' else 'collapsed'}")
        ) for i in range(8)
    ]

    # Crear un Column con los ExpansionTiles
    expansion_column = Column(
        controls=expansion_tiles,
        spacing=10,
        expand=True
    )

    # Crear la barra de navegación inferior
    nav_bar = create_nav_bar(page)

    # Crear un contenedor principal que ocupe todo el espacio disponible
    main_container = Container(
        content=ft.Column(
            controls=[
                nav_top,  # Agregar la barra de navegación superior
                expansion_column,  # Agregar los ExpansionTiles
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

ft.app(target=main)