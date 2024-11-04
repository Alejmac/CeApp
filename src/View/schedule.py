import flet as ft
from flet import Page, Column, Text, Container, Tabs, Tab, DataTable, DataColumn, DataRow, DataCell, ListView,View
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.schedule_ViewModel import ScheduleViewModel  # Importar la clase ScheduleViewModel
import os

def create_tab_content(day_schedule):
    # Crear el DataTable
    data_table = create_data_table(day_schedule)

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
        expand=True,
        margin=ft.margin.only(top=10, bottom=20)  # Margen superior de 20 píxeles
    )

    return container

def create_data_table(day_schedule):
    # Crear las columnas del DataTable
    columns = [
        DataColumn(Text("Hora", color=ft.colors.BLACK, size=12)),
        DataColumn(Text("       Materia", color=ft.colors.BLACK, size=12)),
        DataColumn(Text("Salon", color=ft.colors.BLACK, size=12))
    ]

    # Crear las filas del DataTable
    rows = [
        DataRow(
            cells=[
                DataCell(Container(content=Text(time.replace("-", ""), color=ft.colors.BLACK, size=8, height=60), margin=ft.margin.all(13))),  # Hora
                DataCell(Container(content=Text(details.get("materia", ""), color=ft.colors.BLACK, size=8, height=60), margin=ft.margin.all(13))),  # Materia
                DataCell(Container(content=Text(", ".join(details.get("materia_data", "").split(", ")[1:3]), color=ft.colors.BLACK, size=8, height=60), margin=ft.margin.all(13)))  # Materia Data (valores 1 y 2)
            ]
        ) for time, details in day_schedule.items()
    ]

    # Agregar una fila adicional al final
    rows.append(
        DataRow(
            cells=[
                DataCell(Text("")),
                DataCell(Text("")),
                DataCell(Text(""))
            ]
        )
    )

    # Crear el DataTable
    data_table = DataTable(
        width=900,
        columns=columns,  # Asegurar que el DataTable tenga columnas visibles
        rows=rows,
        divider_thickness=1,
        column_spacing=10,  # Aumentar el espaciado entre columnas
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=50,
        data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
        show_checkbox_column=False,
        expand=True  # Asegurar que el DataTable se expanda
    )

    return data_table

def ScheduleView(page: ft.Page):
  
    # Ajustar el tamaño de la ventana a la resolución del iPhone 15
    page.window.width = 390
    page.window.height = 844

    nav_top= create_nav_top(page)

    nav_bar = create_nav_bar(page)

    # Crear el ViewModel
    view_model = ScheduleViewModel()

    # Crear las pestañas para cada día de la semana
    tabs = Tabs(
        tabs=[
            Tab(text="Lunes", content=create_tab_content(view_model.get_day_schedule("Lunes"))),
            Tab(text="Martes", content=create_tab_content(view_model.get_day_schedule("Martes"))),
            Tab(text="Miércoles", content=create_tab_content(view_model.get_day_schedule("Miercoles"))),
            Tab(text="Jueves", content=create_tab_content(view_model.get_day_schedule("Jueves"))),
            Tab(text="Viernes", content=create_tab_content(view_model.get_day_schedule("Viernes"))),
            Tab(text="Sábado", content=create_tab_content(view_model.get_day_schedule("Sábado")))
        ],
        expand=True,
        indicator_color=ft.colors.WHITE,
        label_color=ft.colors.WHITE,
        unselected_label_color=ft.colors.WHITE,
        height=50  
    )

    # Envolver las pestañas en un contenedor con fondo naranja
    tabs_container = Container(
        content=tabs,
        bgcolor=ft.colors.ORANGE,
        border_radius=ft.border_radius.all(10),  # Bordes redondeados
        padding=ft.padding.all(5),
        margin=ft.margin.only(bottom=40),  # Padding opcional
        expand=True  # Asegurar que el contenedor se expanda
    )

    # Crear un contenedor principal que ocupe todo el espacio disponible
    main_container = Container(
        content=ft.Column(
            controls=[nav_top,
                Container(
                    content=Text("Horario", size=24, weight="bold", color=ft.colors.BLUE),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20 , bottom=30)
                ),
                Container(
                    content=tabs_container,
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

    page.update()
    return View("/schedule", [main_container],bgcolor="#F1DEC6",padding=0, spacing=0)
 #if __name__ == "__main__":
 #   ft.app(target=ScheduleView)