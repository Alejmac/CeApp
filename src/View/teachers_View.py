import flet as ft
from flet import Page, Column, Text, ListTile, ExpansionTile, Container

def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0
    page.bgcolor = ft.colors.WHITE  # Línea donde se cambia el fondo a blanco

    def handle_expansion_tile_change(e):
        page.open(
            ft.SnackBar(
                ft.Text(f"ExpansionTile was {'expanded' if e.data=='true' else 'collapsed'}"),
                duration=1000,
            )
        )
        if e.control.trailing:
            e.control.trailing.name = (
                ft.icons.ARROW_DROP_DOWN
                if e.control.trailing.name == ft.icons.ARROW_DROP_DOWN_CIRCLE
                else ft.icons.ARROW_DROP_DOWN_CIRCLE
            )
            page.update()

    def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

    # Definir los encabezados de la tabla
    headers = ["Div. de Mat.", "Profesor", "Correo", "Grupo", "Tipo", "Tipo Apond"]

    # Crear las filas de la tabla
    rows = [
        ["Materia 1", "Div. de Mat. 1", "Profesor 1", "Correo 1", "Grupo 1", "Tipo 1", "Tipo Apond 1"],
        ["Materia 2", "Div. de Mat. 2", "Profesor 2", "Correo 2", "Grupo 2", "Tipo 2", "Tipo Apond 2"],
        ["Materia 3", "Div. de Mat. 3", "Profesor 3", "Correo 3", "Grupo 3", "Tipo 3", "Tipo Apond 3"],
        ["Materia 4", "Div. de Mat. 4", "Profesor 4", "Correo 4", "Grupo 4", "Tipo 4", "Tipo Apond 4"],
        ["Materia 5", "Div. de Mat. 5", "Profesor 5", "Correo 5", "Grupo 5", "Tipo 5", "Tipo Apond 5"],
        ["Materia 6", "Div. de Mat. 6", "Profesor 6", "Correo 6", "Grupo 6", "Tipo 6", "Tipo Apond 6"],
        ["Materia 7", "Div. de Mat. 7", "Profesor 7", "Correo 7", "Grupo 7", "Tipo 7", "Tipo Apond 7"]
    ]

    # Crear los ExpansionTiles para cada fila
    expansion_tiles = [
        ExpansionTile(
            title=Text(row[0], size=14, weight="bold", color=ft.colors.BLACK),
            subtitle=Text("Información adicional"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            collapsed_text_color=ft.colors.RED,
            text_color=ft.colors.RED,
            controls=[
                ListTile(title=Text(f"{headers[j]}: {cell}", size=12)) for j, cell in enumerate(row[1:])
            ],
            on_change=handle_expansion_tile_change
        ) for row in rows
    ]

    # Crear un Column con scroll
    scrollable_column = Column(
        controls=expansion_tiles,
        spacing=10,
        height=400,  # Ajustar la altura según sea necesario
        width=300,  # Ajustar el ancho según sea necesario
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
    )

    # Crear un contenedor centrado con separación de 20 px en cada lado, margen y bordes redondeados
    container = Container(
        content=scrollable_column,
        padding=20,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.BLACK),  # Margen negro
        border_radius=10,  # Bordes redondeados
        margin=ft.margin.all(20)  # Margen de 20 px en cada lado
    )

    # Ajustar el tamaño de la ventana a la resolución del iPhone 15 con margen
    page.window_width = 390 - 40  # Ancho del iPhone 15 menos el margen
    page.window_height = 844 - 40  # Altura del iPhone 15 menos el margen

    # Agregar el contenedor a la página
    page.add(container)

ft.app(target=main)