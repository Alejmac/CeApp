import flet as ft
from flet import Page, Column, Text, Container, ScrollMode, Icon, icons
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar  # Importar la función create_nav_bar
from ViewModel.data_student_ViewModel import DataStudentViewModel  # Importar la clase DataStudentViewModel
import os

class DataStudentView:
    def __init__(self, main_instance):
        self.main_instance = main_instance  # Almacenar la instancia principal
        self.page = None  # Inicializar el atributo page
        self.controls = []

    def build(self, page: Page):
        self.page = page
        page.spacing = 0
        page.padding = 0
        page.bgcolor = "#F1DEC6"  # Cambiar el color de fondo de la página

        # Ajustar el tamaño de la ventana a la resolución del iPhone 15
        page.window.width = 390
        page.window.height = 844

        # Crear la barra de navegación superior
        create_nav_top(page)

        # Crear la barra de navegación inferior
        nav_bar = create_nav_bar(page)
        nav_bar.width = page.window.width  # Establecer el ancho de nav_bar

        # Crear el ViewModel
        view_model = DataStudentViewModel()
        datos_estudiante = view_model.get_data_as_dict()

        # Obtener los valores necesarios
        nombre = datos_estudiante.get("Nombre", "N/A")
        registro = datos_estudiante.get("Registro", "N/A")
        carrera = datos_estudiante.get("Carrera", "N/A")
        nivel_educativo = datos_estudiante.get("NivelEducativo", "N/A")
        semestre = datos_estudiante.get("Semestre", "N/A")
        estado_alumno = datos_estudiante.get("EstadoAlumno", "N/A")
        tipo_alumno = datos_estudiante.get("TipoAlumno", "N/A")
        estatus_pago = datos_estudiante.get("EstatusPago", "N/A")
        plantel = datos_estudiante.get("Plantel", "N/A")
        area_formacion = datos_estudiante.get("AreaFormacion", "N/A")
        nivel = datos_estudiante.get("Nivel", "N/A")
        plan_estudios = datos_estudiante.get("PlanEstudios", "N/A")
        turno = datos_estudiante.get("Turno", "N/A")
        tipo_plan = datos_estudiante.get("TipoPlan", "N/A")
        tipo_ingreso = datos_estudiante.get("TipoIngreso", "N/A")
        tutor = datos_estudiante.get("Tutor", "N/A")
        correo_academico = datos_estudiante.get("CorreoAcamicoGmail", "N/A")
        correo_institucional = datos_estudiante.get("CorreoInstitucionalMicrosoft", "N/A")
        correo_personal = datos_estudiante.get("CorreoPersonal", "N/A")

        # Crear un contenedor principal con scroll
        main_container = Container(
            content=Column(
                controls=[
                    Container(
                        content=Icon(
                            name=icons.PERSON,
                            size=40,
                            color=ft.colors.BLUE
                        ),
                        width=page.window.width - 30,  # Ancho total menos 30px (15px de cada lado)
                        height=60,
                        bgcolor=ft.colors.GREY,
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(10),  # Bordes redondeados
                        margin=ft.margin.symmetric(horizontal=15)  # Margen de 15px a los lados
                    ),
                    Container(
                        content=Text(f"{nombre}", size=14, weight="bold", color=ft.colors.BLACK),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=10)
                    ),
                    Container(
                        content=Text(f"{registro}", size=14, weight="bold", color=ft.colors.BLACK),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=4)
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(f"Carrera: {carrera}", size=14, weight="bold", color=ft.colors.WHITE),
                                Text(f"Nivel Educativo: {nivel_educativo}", size=14, weight="bold", color=ft.colors.WHITE),
                                Text(f"Semestre: {semestre}", size=14, weight="bold", color=ft.colors.WHITE),
                                Text(f"Estado del Alumno: {estado_alumno}", size=14, weight="bold", color=ft.colors.WHITE)
                            ],
                            spacing=5
                        ),
                        width=page.window.width - 30,  # Ancho total menos 30px (15px de cada lado)
                        bgcolor=ft.colors.BLUE,
                        padding=ft.padding.all(10),
                        margin=ft.margin.only(top=20, left=15, right=15),  # Margen de 15px a los lados
                        alignment=ft.alignment.center_left,
                        border_radius=ft.border_radius.all(10)  # Bordes redondeados
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(f"Área de Formación: {area_formacion}", size=14, weight="bold", color=ft.colors.BLACK),
                                Text(f"Nivel: {nivel}", size=14, weight="bold", color=ft.colors.BLACK),
                                Text(f"Plan de Estudios: {plan_estudios}", size=14, weight="bold", color=ft.colors.BLACK),
                                Text(f"Turno: {turno}", size=14, weight="bold", color=ft.colors.BLACK)
                            ],
                            spacing=5
                        ),
                        width=page.window.width - 30,  # Ancho total menos 30px (15px de cada lado)
                        bgcolor=ft.colors.WHITE,
                        padding=ft.padding.all(10),
                        margin=ft.margin.only(top=20, left=15, right=15),  # Margen de 15px a los lados
                        alignment=ft.alignment.center_left,
                        border_radius=ft.border_radius.all(10)  # Bordes redondeados
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(f"Tipo de Plan: {tipo_plan}", size=14, weight="bold", color=ft.colors.WHITE),
                                Text(f"Tipo de Ingreso: {tipo_ingreso}", size=14, weight="bold", color=ft.colors.WHITE),
                                Text(f"Tutor: {tutor}", size=14, weight="bold", color=ft.colors.WHITE)
                            ],
                            spacing=5
                        ),
                        width=page.window.width - 30,  # Ancho total menos 30px (15px de cada lado)
                        bgcolor=ft.colors.BLUE,
                        padding=ft.padding.all(10),
                        margin=ft.margin.only(top=10, left=15, right=15),  # Margen de 15px a los lados
                        alignment=ft.alignment.center_right,
                        border_radius=ft.border_radius.all(10)  # Bordes redondeados
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(f"Correo Académico: {correo_academico}", size=14, weight="bold", color=ft.colors.BLACK),
                                Text(f"Correo Institucional: {correo_institucional}", size=14, weight="bold", color=ft.colors.BLACK),
                                Text(f"Correo Personal: {correo_personal}", size=14, weight="bold", color=ft.colors.BLACK)
                            ],
                            spacing=5
                        ),
                        width=page.window.width - 30,  # Ancho total menos 30px (15px de cada lado)
                        bgcolor=ft.colors.WHITE,
                        padding=ft.padding.all(10),
                        margin=ft.margin.only(top=20, left=15, right=15),  # Margen de 15px a los lados
                        alignment=ft.alignment.center_left,
                        border_radius=ft.border_radius.all(10)  # Bordes redondeados
                    )
                ],
                expand=True,
                spacing=10,
                scroll=ScrollMode.ALWAYS
            ),
            expand=True,
            margin=ft.margin.only(top=10, bottom=10)  # Ajustar el margen para que no se superponga con el top y el nav
        )

        # Agregar el contenedor principal a la página
        page.add(main_container)
        page.add(nav_bar)  # Agregar la barra de navegación inferior
        self.controls = [main_container]  # Guardar los controles para manejar la visibilidad

# Ejemplo de uso
def main(page: Page):
    view = DataStudentView(None)  # Pasar None como instancia principal para pruebas
    view.build(page)

if __name__ == "__main__":
    ft.app(target=main)