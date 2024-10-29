import flet as ft
from flet import Page, Column, Text, Container, Tabs, Tab, DataTable, DataColumn, DataRow, DataCell, ListView
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.schedule_ViewModel import ScheduleViewModel  # Importar la clase ScheduleViewModel
import os

class ScheduleView:
    def __init__(self, main_instance):
        self.main_instance = main_instance  # Almacenar la instancia principal
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        self.page = page
        page.spacing = 0
        page.padding = 0
        page.bgcolor = ft.colors.ORANGE_50

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window.width = 390
        page.window.height = 844

        # Crear la barra de navegación superior
        create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)
        nav_bar.width = page.window.width  # Establecer el ancho de nav_bar

        # Crear el ViewModel
        view_model = ScheduleViewModel()

        # Crear las pestañas para cada día de la semana
        tabs = Tabs(
            tabs=[
                Tab(text="Lunes", content=self.create_tab_content(view_model.get_day_schedule("Lunes"))),
                Tab(text="Martes", content=self.create_tab_content(view_model.get_day_schedule("Martes"))),
                Tab(text="Miércoles", content=self.create_tab_content(view_model.get_day_schedule("Miércoles"))),
                Tab(text="Jueves", content=self.create_tab_content(view_model.get_day_schedule("Jueves"))),
                Tab(text="Viernes", content=self.create_tab_content(view_model.get_day_schedule("Viernes"))),
                Tab(text="Sábado", content=self.create_tab_content(view_model.get_day_schedule("Sábado")))
            ],
            expand=True,
            indicator_color=ft.colors.WHITE,
            label_color=ft.colors.WHITE,
            unselected_label_color=ft.colors.WHITE,
            height=50  # Ajustar la altura de las pestañas
        )

        # Crear un contenedor principal que ocupe todo el espacio disponible
        main_container = Container(
            content=ft.Column(
                controls=[
                    Container(
                        content=Text("Horario", size=24, weight="bold", color=ft.colors.BLUE),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=20)
                    ),
                    Container(
                        content=tabs,
                        expand=True  # Asegurar que las pestañas se expandan
                    ),
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

    def create_tab_content(self, day_schedule):
        # Crear el DataTable
        data_table = self.create_data_table(day_schedule)

        # Crear un ListView con scroll que contenga el DataTable
        list_view = ListView(
            controls=[data_table],
            expand=True
        )

        # Crear un contenedor blanco que contenga el ListView
        container = Container(
            content=list_view,
            bgcolor=ft.colors.WHITE,
            padding=ft.padding.all(10),
            border_radius=ft.border_radius.all(10),
            expand=True
        )

        return container

    def create_data_table(self, day_schedule):
        # Crear las columnas del DataTable
        columns = [
            DataColumn(Text("Hora", color=ft.colors.BLACK, size=12)),
            DataColumn(Text("Materia", color=ft.colors.BLACK, size=12))
        ]

        # Crear las filas del DataTable
        rows = [
            DataRow(
                cells=[
                    DataCell(Text(time, color=ft.colors.BLACK, size=12)),
                    DataCell(Text(", ".join(f"{key}: {value}" for key, value in details.items()), color=ft.colors.BLACK, size=12))
                ]
            ) for time, details in day_schedule.items()
        ]

        # Crear el DataTable
        data_table = DataTable(
            columns=columns,  # Asegurar que el DataTable tenga columnas visibles
            rows=rows,
            divider_thickness=1,
            column_spacing=10,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            show_checkbox_column=False,
            expand=True  # Asegurar que el DataTable se expanda
        )

        return data_table

# Ejemplo de uso
def main(page: Page):
    view = ScheduleView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)