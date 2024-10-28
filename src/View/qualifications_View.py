import flet as ft
from flet import Page, Column, Text, Container, ScrollMode, IconButton, icons, AlertDialog, DataTable, DataColumn, DataRow, DataCell
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
        page.bgcolor = "#F1DEC6"  # Cambiar el color de fondo de la página

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
        materias = view_model.get_materias()
        primer_parcial = view_model.get_primer_parcial()
        segundo_parcial = view_model.get_segundo_parcial()
        tercer_parcial = view_model.get_tercer_parcial()
        schedule = view_model.get_schedule()

        # Crear los contenedores para cada colección de calificaciones, omitiendo el último
        collection_containers = [
            self.create_collection_container(materias[i], primer_parcial[i], segundo_parcial[i], tercer_parcial[i], schedule.get(materias[i], {}), i)
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
            margin=ft.margin.only(top=20),  # Margen superior de 20px
            padding=ft.padding.all(0)  # Sin padding alrededor del contenedor principal
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)
        self.controls = [main_container]  # Guardar los controles para manejar la visibilidad

    def create_collection_container(self, materia, primer_parcial, segundo_parcial, tercer_parcial, collection, index):
        # Crear el subtítulo con el valor de la clave "materia"
        subtitle = Text(f"{materia}", size=12, weight="bold", color=ft.colors.BLACK)  # Reducir el tamaño del texto

        # Crear los subcontenedores con la información de los parciales
        subcontainers = [
            Container(
                content=Text(f"{primer_parcial}", size=10),  # Mostrar solo el valor
                padding=ft.padding.all(15),  # Hacer el triple de grande
                bgcolor=ft.colors.WHITE,  # Fondo blanco
                border=ft.border.all(1, ft.colors.BLACK),
                alignment=ft.alignment.center,  # Centrar el contenido
                border_radius=ft.border_radius.all(8)  # Redondeo de 8px
            ),
            Container(
                content=Text(f"{segundo_parcial}", size=10),  # Mostrar solo el valor
                padding=ft.padding.all(15),  # Hacer el triple de grande
                bgcolor=ft.colors.WHITE,  # Fondo blanco
                border=ft.border.all(1, ft.colors.BLACK),
                alignment=ft.alignment.center,  # Centrar el contenido
                border_radius=ft.border_radius.all(8)  # Redondeo de 8px
            ),
            Container(
                content=Text(f"{tercer_parcial}", size=10),  # Mostrar solo el valor
                padding=ft.padding.all(15),  # Hacer el triple de grande
                bgcolor=ft.colors.WHITE,  # Fondo blanco
                border=ft.border.all(1, ft.colors.BLACK),
                alignment=ft.alignment.center,  # Centrar el contenido
                border_radius=ft.border_radius.all(8)  # Redondeo de 8px
            )
        ]

        # Crear el botón con el ícono
        button = IconButton(
            icon=icons.INFO,
            on_click=lambda e: self.show_alert_dialog(collection)
        )

        # Determinar el color de fondo del contenedor principal
        bgcolor = ft.colors.GREY_200 if index % 2 == 0 else ft.colors.GREY

        # Crear un contenedor para la colección
        collection_container = Container(
            content=ft.Column(
                controls=[
                    Container(
                        content=ft.Row(
                            controls=[subtitle, button],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        alignment=ft.alignment.center,  # Centrar el título de la materia
                        border_radius=ft.border_radius.all(8)  # Redondeo de 8px
                    ),
                    ft.Row(  # Colocar los contenedores horizontalmente
                        controls=subcontainers,
                        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los subcontenedores
                        spacing=0  # Sin separación entre los subcontenedores
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0  # Sin separación entre los contenedores
            ),
            padding=ft.padding.all(0),  # Sin padding
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=ft.border_radius.all(8),  # Redondeo de 8px
            margin=ft.margin.all(0),  # Sin margen
            bgcolor=bgcolor  # Fondo gris claro o más oscuro
        )

        return collection_container

    def show_alert_dialog(self, collection):
        # Crear las columnas de la DataTable
        columns = [DataColumn(Text(key)) for key in collection.keys()]

        # Crear las filas de la DataTable
        rows = [DataRow(cells=[DataCell(Text(str(value))) for value in collection.values()])]

        # Crear la DataTable
        data_table = DataTable(columns=columns, rows=rows)

        # Crear el AlertDialog
        dialog = AlertDialog(
            title=Text("Detalles de la Colección"),
            content=data_table,
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: self.close_dialog(dialog))
            ]
        )

        # Mostrar el AlertDialog
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    def close_dialog(self, dialog):
        dialog.open = False
        self.page.update()

# Ejemplo de uso
def main(page: Page):
    view = QualificationsView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)