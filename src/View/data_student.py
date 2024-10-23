import flet as ft
from flet import Page

from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from View.nav_top_View import create_nav_top  # Importar la función create_nav_top

class DataStudentView:
    def __init__(self, main_instance):
        self.main_instance = main_instance  # Almacenar la instancia principal
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        page.spacing = 0
        page.padding = 0
        self.page = page
        page.title = "Datos del Alumno"
        page.vertical_alignment = "start"
        page.horizontal_alignment = "center"
        page.bgcolor = ft.colors.WHITE

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window_width = 390
        page.window_height = 844

        # Crear la barra de navegación superior
        nav_top = create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)

        # Crear el ícono de newspaper_outline
        user_icon = ft.Icon(name=ft.icons.PERM_IDENTITY_OUTLINED, size=70, color=ft.colors.BLACK)

        # Crear la lista de CupertinoListTile
        cupertino_list = ft.ListView(
            controls=[
                ft.Container(
                    content=ft.CupertinoListTile(
                        trailing=ft.Icon(name=ft.icons.NEWSPAPER_OUTLINED, color=ft.colors.BLACK),
                        title=ft.Text(f"Clave {i+1}", color=ft.colors.BLACK),
                        subtitle=ft.Text(f"Valor {i+1}", color=ft.colors.BLACK)
                    ),
                    margin=ft.margin.all(2),
                    border_radius=5,
                    border=ft.border.all(1, ft.colors.BLACK)  # Margen delgado alrededor de cada CupertinoListTile
                ) for i in range(20)
            ],
            expand=True
        )

        # Crear el contenedor con la lista y el scroll
        scroll_container = ft.Container(
            content=cupertino_list,
            margin=ft.margin.all(5),  # Agregar margen alrededor de la lista
            #border=ft.border.all(1, ft.colors.BLACK),  # Agregar borde negro
            expand=True
        )

        # Crear el contenedor principal
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    nav_top,  # Agregar la barra de navegación superior
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                user_icon,
                                scroll_container
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.WHITE,
                        padding=5,
                        border_radius=10,
                        expand=True
                    ),
                    nav_bar  # Agregar la barra de navegación inferior
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            expand=True
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)
        self.controls = [main_container]  # Guardar los controles para manejar la visibilidad

# Ejemplo de uso
def main(page: Page):
    view = DataStudentView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)