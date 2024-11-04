import flet as ft
from flet import Page, Column, Text, Container, ScrollMode, Icon, icons,View
from View.nav_top_View import create_nav_top
from View.nav_bar_View import create_nav_bar   
from ViewModel.data_student_ViewModel import DataStudentViewModel   
import os
 
def DataStudentView(page: Page):
   # page.spacing = 0
    #page.padding = 0
    #page.bgcolor = "#F1DEC6"  

    page.window.width = 390
    page.window.height = 844

    #nav_top= create_nav_top(page)     
    nav_bar = create_nav_bar(page)
    nav_bar.width = page.window.width 

    view_model = DataStudentViewModel()
    datos_estudiante = view_model.get_data_as_dict()

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
                        size=50,
                        color=ft.colors.BLACK,
                    ),
                    height=90,
                    bgcolor=ft.colors.GREY,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(0),  # Bordes redondeados
                ),
                Container(
                    content=Text(f"{nombre}", size=14, weight="bold", color=ft.colors.BLACK),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10)
                ),
                Container(
                    content=Text(f"{registro}", size=14, weight="bold", color=ft.colors.BLACK),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=3)
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
                    bgcolor=ft.colors.BLUE,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=20, left=5, right=70),   
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.all(10)  
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
                    bgcolor=ft.colors.WHITE,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=10, left=70, right=10),   
                    alignment=ft.alignment.center_right,
                    border_radius=ft.border_radius.all(10)   
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
                    bgcolor=ft.colors.BLUE,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=10, left=10, right=70),   
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.all(10)   
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
                    bgcolor=ft.colors.WHITE,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=10,  left=70, right=10),  
                    alignment=ft.alignment.center_right,
                    border_radius=ft.border_radius.all(10)   
                ),
            ],
            
            expand=True,
            spacing=22,
            scroll=ScrollMode.ALWAYS,
        ),
        
        expand=True,
        margin=ft.margin.only(top=0, bottom=0)  
    )        
    #page.add(main_container)
    #page.add(nav_bar)  
    return View("/data_student", [main_container],bgcolor="#F1DEC6",padding=0, spacing=0, appbar=nav_bar)

if __name__ == "__main__":
    ft.app(target=DataStudentView)