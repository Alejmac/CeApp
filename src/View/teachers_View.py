import flet as ft
from flet import Page, Column, Text, Container, ElevatedButton, BottomSheet, ScrollMode
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.teacher_ViewModel import TeacherViewModel  # Importar la clase TeacherViewModel
import os

class TeachersView:
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

        # Obtener los datos de los profesores desde el ViewModel
        view_model = TeacherViewModel()
        datos_profesores = view_model.get_teachers()

        # Crear los botones para cada materia
        buttons = []
        for profesor, items in datos_profesores.items():
            for materia in items['materias']:
                buttons.append(
    ElevatedButton(
        text=materia['nombre'],
        on_click=lambda e, profesor=profesor, items=items: self.show_bottom_sheet(e, items),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.WHITE,
            color=ft.colors.BLACK,
            padding=ft.padding.all(15),
            elevation=20,
            text_style=ft.TextStyle(
                size=12,  # Tamaño de la letra más pequeño
                #align=ft.TextAlign.CENTER  # Centrar el texto
            )
        ),
        width=300,  # Ancho del botón
        height=50,  # Altura del botón
    )
)


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
            margin=ft.margin.only(top=20, left=13)  # Separación de 20 px arriba y 10 px a la izquierda
        )

        # Crear un título "Materias"
# Crear un título "Materias"
        title_container = Container(
    content=Text(
        "Materias",
        size=30,
        weight="bold",
        color=ft.colors.ORANGE_300,
        font_family="DM Serif Display",  # Cambiar el estilo de letra
        #decoration=ft.TextDecoration.UNDERLINE  # Remarcar en negro
    ),
    alignment=ft.alignment.center,  # Centrar el título
    margin=ft.margin.only(top=60, bottom=0)  # Margen superior de 30 px y sin margen inferior
)

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    title_container,  # Agregar el título
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

    def show_bottom_sheet(self, e, items):
        # Crear el contenido del BottomSheet
        bottom_sheet_content = Column(
            controls=[
                self.create_data_table(items)
            ],
            spacing=10,
            scroll=ScrollMode.ALWAYS  # Habilitar el scroll dentro del BottomSheet
        )

        # Crear un Container para ajustar la altura del BottomSheet
        bottom_sheet_container = Container(
            content=bottom_sheet_content,
            height=800,  # Ajustar la altura del BottomSheet
            bgcolor=ft.colors.WHITE,  # Cambiar el color de fondo a blanco
            border_radius=ft.border_radius.all(20)  # Redondear las esquinas
        )

        # Crear el BottomSheet
        bottom_sheet = BottomSheet(
            content=bottom_sheet_container,
            open=True,
            on_dismiss=lambda e: print("BottomSheet cerrado")
        )

        # Agregar el BottomSheet a la página
        self.page.overlay.append(bottom_sheet)
        self.page.update()

    def create_data_table(self, items):
        # Crear las columnas del DataTable
        columns = [
            ft.DataColumn(ft.Text("Campo", color=ft.colors.BLACK)),
            ft.DataColumn(ft.Text("__________________________________", color=ft.colors.BLACK))
        ]

        # Crear las filas del DataTable
        rows = []
        for materia in items['materias']:
            rows.extend([
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Clave", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['clave'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Nombre", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['nombre'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("División", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['division'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grupo", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['grupo'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Tipo", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['tipo'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Tipo Ponderación", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['tipo_pond'], color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Primer Parcial", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['primer_parcial'] or '', color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Segundo Parcial", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['segundo_parcial'] or '', color=ft.colors.BLACK))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Tercer Parcial", color=ft.colors.BLACK)),
                        ft.DataCell(ft.Text(materia['tercer_parcial'] or '', color=ft.colors.BLACK))
                    ]
                )
            ])

        # Crear el DataTable
        data_table = ft.DataTable(
            columns=columns,
            rows=rows,
            divider_thickness=1,  # Línea divisoria en medio
            column_spacing=10,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={ft.ControlState.HOVERED: "white"},
            show_checkbox_column=False,
        )

        return data_table

# Ejemplo de uso
def main(page: Page):
    view = TeachersView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)