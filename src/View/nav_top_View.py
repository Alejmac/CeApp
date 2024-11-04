import flet as ft
from flet import Container, IconButton, Text, Row, icons, colors

def create_nav_top(page):
    # Función para manejar el clic en el botón de perfil
    def on_profile_click(e):
        print("se presionó")

    # Crear el botón de icono
    icon_button = IconButton(
        icon=icons.PERM_IDENTITY_OUTLINED,
        #on_click=on_profile_click,
        on_click=lambda _: page.go("/data_student"),
        icon_color=colors.WHITE
    )

    # Crear el texto con el título "CeApp"
    title_text = Text(
        "CeApp",
        size=24,
        weight="bold",
        color=colors.WHITE,
        font_family="DM Serif Display"  # Cambiar el estilo de letra
    )

    # Crear el contenedor
    nav_top_container = Container(
        content=Row(
            controls=[
                title_text,
                icon_button
            ],
            alignment="spaceBetween"
        ),
        bgcolor="#4158A6",
        padding=ft.padding.all(10),
        alignment=ft.alignment.center
    )

    # Devolver el contenedor
    return nav_top_container

# Exportar la función para que pueda ser importada en otros archivos
__all__ = ["create_nav_top"]