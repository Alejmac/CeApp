import flet as ft
from flet import *
import os
 
# Construir la ruta de la imagen
image_path = os.path.join(os.getcwd(), "Img", "entrada.jpg")

def FirstView(page: Page):
    page.title = "Explora la Nueva App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = colors.BLACK

    # Verifica si la imagen existe
    if not os.path.exists(image_path):
        print(f"Error: La imagen '{image_path}' no se encuentra.")
    else:
        print(f"Imagen encontrada: {image_path}")

    # Contenedor de la imagen con degradado
    image_container = ft.Container(
        content=ft.Stack(
            [
                ft.Image(
                    src=image_path,
                    fit=ft.ImageFit.COVER,
                    width=page.width,
                    height=page.height
                ),
                ft.Container(
                    content=None,
                    gradient=ft.LinearGradient(
                        begin=alignment.top_center,
                        end=alignment.bottom_center,
                        colors=[ft.colors.TRANSPARENT, ft.colors.BLACK]
                    ),
                    width=page.width,
                    height=page.height
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                ft.Text(
                                    "Explora la Nueva App",
                                    size=40,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.LEFT
                                ),
                                margin=ft.margin.only(top=100)
                            ),
                            ft.Container(
                                ft.IconButton(
                                    icon=ft.icons.ARROW_FORWARD,
                                    icon_size=30,
                                    icon_color=ft.colors.BLACK,
                                    bgcolor=ft.colors.WHITE,
                                    on_click=lambda _: page.go("/login"),  
                                ),
                                margin=ft.margin.only(top=15),
                                alignment=alignment.center
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    alignment=alignment.top_left,
                    padding=ft.padding.all(20)
                )
            ]
        ),
        width=page.width,
        height=page.height
    )

    # Devolver el objeto View
    return View(
        "/first",
        [image_container]
    )
#if __name__ == "__main__":
   # ft.app(target=FirstView)