import json
import requests
from bs4 import BeautifulSoup
import os
from kivy.utils import platform
from plyer import storagepath

def clean_text(text):
    """Función para limpiar texto eliminando caracteres no deseados."""
    return text.replace('\xa0', '').replace('\n', '').strip()

def extraer_keys():
    """Función para extraer las claves de la tabla."""
    keys = [
        "CLAVE",
        "NIVEL",
        "MATERIA",
        "PROFESOR",
        "ESTATUS MATERIA",
        "TIPO POND.",
        "1ER. PARCIAL (Faltas)",
        "1ER. PARCIAL (Calf. Captura)",
        "1ER. PARCIAL (Calf. Pond.)",
        "2DO. PARCIAL (Faltas)",
        "2DO. PARCIAL (Calf. Captura)",
        "2DO. PARCIAL (Calf. Pond.)",
        "3RO. PARCIAL (Faltas)",
        "3RO. PARCIAL (Calf. Captura)",
        "3RO. PARCIAL (Calf. Pond.)",
        "FINAL (Faltas)",
        "FINAL (Calf.)"
    ]
    return keys

def parsear_tabla(soup, table):
    """Función para parsear la tabla y convertirla en un diccionario JSON."""
    keys = extraer_keys()
    grades_json = {}

    tr_elements = table.find_all('tr')[2:]  # Saltar las filas de encabezado

    for tr in tr_elements:
        td_elements = tr.find_all('td')
        if td_elements:
            values = []
            for td in td_elements:
                center = td.find('center')
                text = clean_text(center.text if center else td.text)
                # Reemplazar texto vacío por "-"
                values.append(text if text else "-")

            # Ajustar el número de valores para que coincida con el número de claves
            if len(values) < len(keys):
                values.extend(["-"] * (len(keys) - len(values)))
            elif len(values) > len(keys):
                values = values[:len(keys)]

            # Crear un diccionario con los valores correspondientes
            grade_dict = {}
            for i, key in enumerate(keys):
                grade_dict[key] = values[i]

            # Asignar la clave correspondiente al primer valor y repetirla dentro del diccionario
            key = values[0]
            grade_dict['CLAVE'] = key
            if 'REPORTE DE CALIFICACIONES' in grade_dict:
                del grade_dict['REPORTE DE CALIFICACIONES']
            grades_json[key] = grade_dict

    return grades_json

def obtener_calificaciones( registro, password):
    url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/calificaciones'

    datos_post = {'registro': registro, 'password': password}

    try:
        sesion = requests.Session()
        response_login = sesion.post(url_login, data=datos_post)
        response_login.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud de login: {e}")
        return None

    try:
        response_home = sesion.get(url_home)
        response_home.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

    soup = BeautifulSoup(response_home.content, 'html.parser')



    # Buscar el div con id 'cal'
    div_cal = soup.find('div', {'id': 'cal'})
    if div_cal is None:
        raise ValueError("No se encontró ningún div con el id 'cal' en el documento HTML.")

    # Buscar la tabla de calificaciones
    grades_table = div_cal.find('table', {'class': 'tabla'})
    if grades_table is None:
        raise ValueError("No se encontró ninguna tabla con los atributos especificados en el documento HTML.")

    try:
        # Parsear la tabla
        grades_final = parsear_tabla(soup, grades_table)

        # Convertir las calificaciones finales a JSON
        grades_json = json.dumps(grades_final, ensure_ascii=False, indent=2)

        # Guardar el archivo JSON en la carpeta 'Data'
        if platform == 'android' or platform == 'ios':
            data_folder = storagepath.get_documents_dir()
        else:
            data_folder = os.path.join(os.getcwd(), 'Data')

        os.makedirs(data_folder, exist_ok=True)
        json_file_path = os.path.join(data_folder, 'qualifications.json')

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(grades_json)

        print(f"Archivo JSON guardado en: {json_file_path}")

    except Exception as e:
        print(f"Se produjo un error: {e}")