import flet as ft
from flet import Page, Column, Text, ExpansionTile, Container
import os
 
from ViewModel.schedule_ViewModel import ScheduleViewModel  # Importar la clase ScheduleViewModel

from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar 


class ScheduleView:
    def __init__(self, main_instance):
        self.main_instance = main_instance  # Almacenar la instancia principal
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        self.page = page
        page.spacing = 0
        page.padding = 0
        page.bgcolor = ft.colors.ORANGE_50

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window_width = 390
        page.window_height = 844

        # Crear la barra de navegación superior
        create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)
        nav_bar.width = page.window_width  # Establecer el ancho de nav_bar

