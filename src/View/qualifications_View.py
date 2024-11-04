import flet as ft
from flet import Page, Column, Text, Container, ScrollMode, icons, AlertDialog, DataTable, DataColumn, DataRow, DataCell, View
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.quialifications_ViewModel import QualificationsViewModel  # Importar la clase QualificationsViewModel
import os

def create_collection_container(materia, primer_parcial, segundo_parcial, tercer_parcial, collection, index):
    # Crear el subtítulo con el valor de la clave "materia"
    subtitle = Text(f"{materia}", size=12, weight="bold", color=ft.colors.BLACK)  # Reducir el tamaño del texto

    # Crear los subcontenedores con la información de los parciales
    subcontainers = [
        Container(
            content=Text(f"{primer_parcial}", size=10,color=ft.colors.BLACK),  # Mostrar solo el valor
            padding=ft.padding.all(15),  # Hacer el triple de grande
            bgcolor=ft.colors.WHITE,  # Fondo blanco
            border=ft.border.all(1, ft.colors.BLACK),
            alignment=ft.alignment.center,  # Centrar el contenido
            border_radius=ft.border_radius.all(8)  # Redondeo de 8px
        ),
        Container(
            content=Text(f"{segundo_parcial}", size=10,color=ft.colors.BLACK),  # Mostrar solo el valor
            padding=ft.padding.all(15),  # Hacer el triple de grande
            bgcolor=ft.colors.WHITE,  # Fondo blanco
            border=ft.border.all(1, ft.colors.BLACK),
            alignment=ft.alignment.center,  # Centrar el contenido
            border_radius=ft.border_radius.all(8)  # Redondeo de 8px
        ),
        Container(
            content=Text(f"{tercer_parcial}", size=10,color=ft.colors.BLACK),  # Mostrar solo el valor
            padding=ft.padding.all(15),  # Hacer el triple de grande
            bgcolor=ft.colors.WHITE,  # Fondo blanco
            border=ft.border.all(1, ft.colors.BLACK),
            alignment=ft.alignment.center,  # Centrar el contenido
            border_radius=ft.border_radius.all(8)  # Redondeo de 8px
        )
    ]

    # Determinar el color de fondo del contenedor principal
    bgcolor = ft.colors.GREY_200 if index % 2 == 0 else ft.colors.GREY

    # Crear un contenedor para la colección
    collection_container = Container(
        content=ft.Column(
            controls=[
                Container(
                    content=ft.Row(
                        controls=[subtitle],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    alignment=ft.alignment.center,  # Centrar el título de la materia
                    border_radius=ft.border_radius.all(8),
                    height=70,   # Redondeo de 8px
                    margin=ft.margin.only(left=10, right=10,) 
                ),
                ft.Row(  # Colocar los contenedores horizontalmente
                    controls=subcontainers,
                    alignment=ft.MainAxisAlignment.CENTER,  # Centrar los subcontenedores
                    spacing=3,  # Sin separación entre los subcontenedores
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0  # Sin separación entre los contenedores
        ),
        padding=ft.padding.all(0),  # Sin padding
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius=ft.border_radius.all(8),  # Redondeo de 8px
        margin=ft.margin.all(0),  # Sin margen
        bgcolor=bgcolor,
            # Fondo gris claro o más oscuro
    )

    return collection_container

def QualificationsView(page: Page):
    page.spacing = 0
    page.padding = 0
    page.bgcolor = "#F1DEC6"  # Cambiar el color de fondo de la página

    # Ajustar el tamaño de la ventana a la resolución del iPhone 15
    page.window.width = 390
    page.window.height = 844

    # Crear la barra de navegación superior
    nav_top = create_nav_top(page)

    # Crear la barra de navegación inferior
    nav_bar = create_nav_bar(page)
    nav_bar.width = page.window.width  # Establecer el ancho de nav_bar

    # Obtener los datos de las calificaciones desde el ViewModel
    view_model = QualificationsViewModel()
    materias = view_model.get_materias()
    primer_parcial = view_model.get_primer_parcial()
    segundo_parcial = view_model.get_segundo_parcial()
    tercer_parcial = view_model.get_tercer_parcial()
    schedule = view_model.get_schedule()

    # Crear los contenedores para cada colección de calificaciones, omitiendo el último
    collection_containers = [
        create_collection_container(materias[i], primer_parcial[i], segundo_parcial[i], tercer_parcial[i], schedule.get(materias[i], {}), i)
        for i in range(len(materias) - 1)
    ]

    # Crear un Column con los contenedores de las colecciones
    collection_column = Column(
        controls=collection_containers,
        expand=True,
        alignment=ft.MainAxisAlignment.START,  # Alinear los contenedores al inicio
        scroll=ScrollMode.ALWAYS,  # Habilitar el scroll
        spacing=0  # Sin separación entre los contenedores
    )

    # Crear un contenedor principal que ocupe todo el espacio disponible
    main_container = Container(
        content=ft.Column(
            controls=[
                nav_top,
                Container(
                    content=Text("Calificaciones", size=24, weight="bold", color=ft.colors.BLUE),  # Título principal con estilo
                    alignment=ft.alignment.center,  # Centrar el título
                    padding=ft.padding.all(10),  # Padding alrededor del título
                    margin=ft.margin.only(bottom=30)  # Separación inferior de 30px
                ),
                collection_column,  # Agregar el Column con los contenedores de las colecciones
                nav_bar  # Agregar la barra de navegación inferior
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0  # Sin separación entre los contenedores
        ),
        expand=True,
        margin=ft.margin.only(top=0),  # Margen superior de 20px
        padding=ft.padding.all(0)  # Sin padding alrededor del contenedor principal
    )

    #page.add(main_container)
    page.update()
    return View("/qualifications", [main_container], bgcolor="#F1DEC6", padding=0, spacing=0)

#if __name__ == "__main__":
#    ft.app(target=QualificationsView)