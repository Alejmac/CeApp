import flet as ft

def create_nav_top(page: ft.Page):
    # Función para manejar el clic en el botón de perfil
    def on_profile_click(e):
        print("se presionó")

    # Crear el botón de perfil de usuario
    profile_button = ft.IconButton(
        icon=ft.icons.PERSON,
        on_click=on_profile_click
    )

    # Crear el texto "CeApp"
    ceapp_text = ft.Text(
        value="CeApp",
        style="headlineMedium",  # Estilo de letra bonita
        color=ft.colors.BLACK
    )

    # Crear el contenedor principal
    nav_container = ft.Container(
        content=ft.Row(
            controls=[
                ceapp_text,
                ft.Container(expand=True),  # Contenedor expandible para empujar el botón a la derecha
                profile_button
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=page.window_width,  # Hacer que el contenedor se adapte al ancho de la ventana
        height=90,  # Altura fija
        padding=ft.padding.all(10),
        bgcolor=ft.colors.GREY_200,
        border_radius=ft.border_radius.all(10)
    )

    return nav_container

# Exportar la función para que pueda ser importada en otros archivos
__all__ = ["create_nav_top"]