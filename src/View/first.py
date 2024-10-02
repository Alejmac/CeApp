import flet as ft
from flet import *
import os
from ViewModel.login_ViewModel import LoginViewModel


image_path = os.path.join(os.getcwd(), "img", "entrada.jpg")

class LoginView:
    def __init__(self):
        self.viewmodel = LoginViewModel()

    def build(self, page: Page):
        self.page = page  # Guardar la referencia de la página

        self.registro_field = ft.TextField(
            width=280,
            height=100,
            hint_text="Registro",
            border=10,
            border_radius=20,
            color="black",
            prefix_icon=ft.icons.EMAIL
        )

        self.password_field = ft.TextField(
            width=280,
            height=100,
            hint_text="Contraseña",
            border=10,
            border_radius=20,
            color="black",
            prefix_icon=ft.icons.LOCK,
            password=True
        )

        image_container = ft.Container(
            content=ft.Image(
                src=image_path,
                fit=ft.ImageFit.COVER,
                width=page.width,
                height=page.height
            ),
            width=page.width,
            height=page.height
        )

        gradient_overlay = ft.Container(
            width=page.width,
            height=page.height,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.BOTTOM_CENTER,
                end=ft.Alignment.TOP_CENTER,
                colors=["#000000", "transparent"]
            )
        )

        login_container = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text(
                        "Iniciar Sesion",
                        width=320,
                        size=30,
                        text_align='center',
                        color="black",
                        weight="w900"
                    ),
                    padding=ft.padding.only(20, 20)
                ),
                ft.Container(
                    self.registro_field,
                    padding=ft.padding.only(20, 20)
                ),
                ft.Container(
                    self.password_field,
                    padding=ft.padding.only(20, 20)
                ),
                ft.Container(
                    ft.Checkbox(
                        label="Recordar Contraseña",
                        check_color="black",
                        fill_color="white",
                        label_style=ft.TextStyle(color="black")  # Color del texto
                    ),
                    padding=ft.padding.only(80)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        text="INICIAR",
                        width=280,
                        bgcolor="#FF8343",
                        on_click=self.on_login_click
                    ),
                    padding=ft.padding.only(20, 20)
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            border_radius=30,
            width=320,
            height=500,
            bgcolor=ft.colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=18,
                blur_radius=15,
                color=ft.colors.BLACK12,
                offset=ft.Offset(0, 5)
            ),
            margin=ft.margin.only(top=-120)  # mover el contenedor hacia arriba
        )

        page.bgcolor = ft.colors.ORANGE_50
        page.vertical_alignment = 'start'
        page.horizontal_alignment = "center"
        page.add(image_container)
        page.add(gradient_overlay)
        page.add(login_container)

    def on_login_click(self, e):
        registro = self.registro_field.value
        password = self.password_field.value

        if self.viewmodel.login(registro, password):
            alert = ft.AlertDialog(
                title=ft.Text("Login Exitoso"),
                content=ft.Text("Bienvenido al sistema del CETI"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: self.close_alert(alert))
                ]
            )
        else:
            alert = ft.AlertDialog(
                title=ft.Text("Login Fallido"),
                content=ft.Text("Usuario o contraseña incorrectos"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: self.close_alert(alert))
                ]
            )
        self.page.overlay.append(alert)
        alert.open = True
        self.page.update()

    def close_alert(self, alert):
        alert.open = False
        self.page.update()

def main(page: Page):
    view = LoginView()
    view.build(page)

ft.app(target=main)