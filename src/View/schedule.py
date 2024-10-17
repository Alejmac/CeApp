import flet as ft
from flet import *
from nav_top_View import create_nav_top  # Importar la función create_nav_top
from nav_bar_View import create_nav_bar  # Importar la función create_nav_bar

class ScheduleView:
    def __init__(self):
        pass

    def build(self, page: Page):
        page.title = "Horario del Alumno"
        page.vertical_alignment = "start"
        page.horizontal_alignment = "center"
        page.bgcolor = ft.colors.ORANGE_50

        # Establecer el tamaño de la ventana
        page.window_width = 390
        page.window_height = 844

        # Crear la barra de navegación superior
        nav_top = create_nav_top(page)

        # Imágenes encima del contenedor superior
        top_icons = ft.Row(
            controls=[
                ft.Image(src="img/lineas.png", width=32, height=32),
                ft.Image(src="img/perfil2.png", width=32, height=32)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=page.window_width
        )

        # Contenedor superior con 6 divisiones horizontales
        top_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(f"Día {i+1}", text_align="center"),
                        expand=True,
                        height=50,
                        bgcolor=ft.colors.GREY_200,  # Parte superior
                        alignment=ft.alignment.center,
                        border=ft.border.all(1, ft.colors.WHITE)  # Borde blanco para divisiones
                    ) for i in range(6)
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=0  # Sin separación entre divisiones
            ),
            margin=ft.margin.only(top=20, left=40),
            width=300,  # Ajustar el ancho para que coincida con el contenedor central
            height=50,
            alignment=ft.alignment.center,  # Centrar el contenedor
            border_radius=ft.border_radius.only(top_left=10, top_right=10, bottom_left=10, bottom_right=10)  # Bordes redondeados solo en las esquinas
        )

        # Contenedor izquierdo con 8 divisiones verticales para las horas
        left_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(f"{8+i}:00", text_align="center"),
                        width=50,
                        height=50,  # Ajustar la altura de cada división
                        bgcolor=ft.colors.ORANGE,  # Contenedor de horarios
                        alignment=ft.alignment.center,
                        border=ft.border.all(1, ft.colors.WHITE)  # Borde blanco para divisiones
                    ) for i in range(8)
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=0  # Sin separación entre divisiones
            ),
            width=50,
            height=400,  # Ajustar la altura total del contenedor izquierdo
            margin=ft.margin.only(top=20, bottom=10),
            border_radius=ft.border_radius.only(top_left=10, top_right=10, bottom_left=10, bottom_right=10)  # Bordes redondeados solo en las esquinas
        )

        # Nuevo contenedor central con GridView de 8 filas y 6 columnas
        central_container = ft.Container(
            content=ft.GridView(
                controls=[
                    ft.Container(
                        content=ft.Text(f"Materia {i+1}", text_align="center"),
                        width=50,  # Ajustar el ancho para que coincida con el contenedor izquierdo
                        height=50,  # Ajustar la altura para que coincida con el contenedor izquierdo
                        bgcolor=ft.colors.GREY,  # Contenedor más grande
                        alignment=ft.alignment.center,
                        border=ft.border.all(1, ft.colors.WHITE),  # Borde blanco para divisiones
                        border_radius=15
                    ) for i in range(48)  # 8 filas * 6 columnas
                ],
                runs_count=6,  # Número de columnas
                spacing=0,  # Sin separación entre cuadritos
                run_spacing=0,  # Sin separación entre filas
                expand=False  # No expandir el GridView
            ),
            width=300,  # Fijar el ancho del contenedor central
            height=400,  # Fijar la altura del contenedor central
            margin=ft.margin.only(top=20, bottom=10, left=5),  # Establecer márgenes
            alignment=ft.alignment.center,  # Centrar el contenedor
            border_radius=ft.border_radius.only(top_left=10, top_right=10, bottom_left=10, bottom_right=10)  # Bordes redondeados solo en las esquinas
        )

        # Barra de navegación inferior
        bottom_navigation = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.HOME, on_click=lambda e: print("Home")),
                    ft.IconButton(icon=ft.icons.SCHEDULE, on_click=lambda e: print("Schedule")),
                    ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda e: print("Settings"))
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            width=page.window_width,
            height=50,
            bgcolor=ft.colors.GREY_200,  # Parte superior
            margin=ft.margin.only(bottom=10, left=0, right=0),  # Quitar margen derecho
            border_radius=ft.border_radius.all(40)  # Bordes redondeados con radio de 40 píxeles
        )

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    nav_top,  # Agregar la barra de navegación superior
                    top_icons,
                    ft.Container(content=top_container, alignment=ft.alignment.center),  # Centrar el contenedor superior
                    ft.Row([left_container, central_container], alignment=ft.MainAxisAlignment.CENTER, spacing=0, expand=True),
                    ft.Container(content=nav_bar, alignment=ft.alignment.bottom_center, margin=ft.margin.all(0), padding=ft.padding.all(0))
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            expand=True
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)

# Crear una instancia de ScheduleView y construir la página
def main(page: Page):
    view = ScheduleView()
    view.build(page)

ft.app(target=main)