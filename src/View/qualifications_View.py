import flet as ft
from flet import Page, Column, Text, Container, ElevatedButton, AlertDialog, TextButton, ScrollMode
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
        datos_calificaciones = view_model.get_qualifications_by_collection()

        # Crear los botones para cada colección de calificaciones
        buttons = [
            ElevatedButton(
                text=f"{collection_name}",
                on_click=lambda e, collection_name=collection_name, items=items: self.show_alert_dialog(e, collection_name, items),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.BLACK,
                    padding=ft.padding.all(15),
                    elevation=10
                ),
                width=150,  # Ancho del botón
                height=50,  # Altura del botón
            ) for collection_name, items in datos_calificaciones.items()
        ]

        # Crear un Column con los botones
        button_column = Column(
            controls=buttons,
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar los botones verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los botones horizontalmente
            scroll=ScrollMode.ALWAYS  # Habilitar el scroll
        )

        # Crear un Container para centrar el Column con los botones
        button_container = Container(
            content=button_column,
            alignment=ft.alignment.center,  # Centrar el Container
            margin=ft.margin.only(top=100, left=50)  # Separación de 100 px arriba y 90 px a la izquierda
        )

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    button_container,  # Agregar el Container con los botones
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

    def show_alert_dialog(self, e, collection_name, items):
        # Crear el contenido del AlertDialog
        content = Column(
            controls=[
                Text(f"{collection_name}", size=20, weight="bold", color=ft.colors.BLACK),
                self.create_data_table(items)
            ],
            spacing=10,
            scroll=ScrollMode.ALWAYS  # Habilitar el scroll dentro del AlertDialog
        )

        # Crear el AlertDialog
        alert_dialog = AlertDialog(
            title=Text(f"Información de {collection_name}"),
            content=content,
            actions=[
                TextButton("Cerrar", on_click=lambda e: self.page.close(alert_dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("AlertDialog cerrado")
        )

        # Abrir el AlertDialog
        self.page.open(alert_dialog)

    def create_data_table(self, items):
        # Crear las columnas del DataTable
        columns = [
            ft.DataColumn(ft.Text("Clave")),
            ft.DataColumn(ft.Text("Valor")),
        ]

        # Crear las filas del DataTable
        rows = [
            ft.DataRow(
                [ft.DataCell(ft.Text(k)), ft.DataCell(ft.Text(v))]
            ) for k, v in items.items()
        ]

        # Crear el DataTable
        data_table = ft.DataTable(
            columns=columns,
            rows=rows,
            divider_thickness=1,  # Línea divisoria en medio
            column_spacing=30,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=80,
            data_row_color={ft.ControlState.HOVERED: "white"},
            show_checkbox_column=False,
        )

        return data_table

# Ejemplo de uso
def main(page: Page):
    view = QualificationsView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)