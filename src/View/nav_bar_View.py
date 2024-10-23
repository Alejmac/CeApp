import flet as ft
from flet import Container, Row, IconButton, icons

def create_nav_bar(page):
    nav_bar = Container(
        content=Row(
            controls=[
                IconButton(
                    icon=icons.HOME,
                    on_click=lambda e: print("Home clicked")
                ),
                IconButton(
                    icon=icons.SCHEDULE,
                    on_click=lambda e: print("Schedule clicked")
                ),
                IconButton(
                    icon=icons.GRADE,
                    on_click=lambda e: print("Qualifications clicked")
                ),
                IconButton(
                    icon=icons.PEOPLE,
                    on_click=lambda e: print("Teachers clicked")
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        bgcolor=ft.colors.GREY_200,
        padding=10
    )

    return nav_bar