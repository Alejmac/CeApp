import flet as ft

def create_nav_top(page: ft.Page):
    # Función para manejar el clic en el botón de perfil
    def on_profile_click(e):
        print("se presionó")

    # Crear el AppBar
    app_bar = ft.AppBar(
        
        leading_width=40,
        title=ft.Text("CeApp", style="headlineMedium", color=ft.colors.BLACK),
        center_title=False,
        bgcolor=ft.colors.GREY_500,
        actions=[
            ft.IconButton(
                icon=ft.icons.PERM_IDENTITY_OUTLINED,
                on_click=on_profile_click
            )
        ]
    )

    # Asignar el AppBar a la página
    page.appbar = app_bar

# Exportar la función para que pueda ser importada en otros archivos
__all__ = ["create_nav_top"]