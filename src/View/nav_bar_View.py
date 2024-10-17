import flet as ft

def create_nav_bar(page: ft.Page):
    # Barra de navegación inferior
    bottom_navigation = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.CALENDAR_TODAY, on_click=lambda e: print("Calendar")),  # Icono de calendario
                ft.IconButton(icon=ft.icons.EVENT_NOTE, on_click=lambda e: print("Agenda")),  # Icono de agenda
                ft.IconButton(icon=ft.icons.LIST, on_click=lambda e: print("List"))  # Icono de lista
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True  # Asegurarse de que el Row se expanda para llenar el contenedor
        ),
        width=page.window.width,
        height=60,
        bgcolor=ft.colors.GREY_200,  # Parte superior
        margin=ft.margin.all(0),  # Sin margen
        padding=ft.padding.all(0),  # Sin padding
        border_radius=ft.border_radius.all(0)  # Sin bordes redondeados
    )

    return bottom_navigation