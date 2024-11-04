import json
import requests
from bs4 import BeautifulSoup
import os
from kivy.utils import platform
from plyer import storagepath
from unidecode import unidecode


def get_session(registro, password):
    url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
    datos_post = {'registro': registro, 'password': password}
    try:
        sesion = requests.Session()
        response_login = sesion.post(url_login, data=datos_post)
        response_login.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud de login: {e}")
        return None
    return sesion

def get_tira_materias(sesion):
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/tiras'
    try:
        response_home = sesion.get(url_home)
        response_home.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

    soup = BeautifulSoup(response_home.content, 'html.parser')
    
    # Buscar la tabla específica de materias asignadas
    tabla_asignadas = soup.find('th', class_='naranja', text=lambda t: "LISTA DE MATERIAS ASIGNADAS PARA EL PERIODO" in t)
    
    if not tabla_asignadas:
        print("No se encontró la tabla de materias asignadas.")
        return None

    # Buscar las filas que contienen las materias asignadas
    materias = []
    filas = tabla_asignadas.find_parent('table').find_all('tr')[2:]  # Ignora el encabezado

    for fila in filas:
        columnas = fila.find_all('td')
        
        if len(columnas) >= 11:
            materia = {
                'clave': columnas[0].text.strip(),
                'nombre': columnas[1].text.strip(),
                'division': columnas[2].text.strip(),
                'profesor': columnas[3].text.strip(),
                'correo': columnas[4].text.strip(),
                'grupo': columnas[5].text.strip(),
                'tipo': columnas[6].text.strip(),
                'tipo_pond': columnas[7].text.strip(),
                'primer_parcial': columnas[8].text.strip() if columnas[8].text.strip() != '---' else None,
                'segundo_parcial': columnas[9].text.strip() if columnas[9].text.strip() != '---' else None,
                'tercer_parcial': columnas[10].text.strip() if columnas[10].text.strip() != '---' else None
            }
            materias.append(materia)

    return materias


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
            if key != "-":
                grades_json[key] = grade_dict

    return grades_json

def get_grades(sesion):
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/calificaciones'

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
        return grades_final

    except Exception as e:
        print(f"Se produjo un error: {e}")


def get_schedule(sesion):
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/horario'

    try:
        response_home = sesion.get(url_home)
        response_home.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

    soup = BeautifulSoup(response_home.content, 'html.parser')

    def clean_text(text):
        return text.strip().replace('\xa0', '')

    def parse_horario_table(table):
        horario_json = {}
        rows = table.find_all('tr')
        
        # Obtener los días de la semana
        dias_semana = [clean_text(th.text) for th in rows[0].find_all('th')]
        
        # Iterar sobre las filas de la tabla, excluyendo la primera fila (encabezados de días)
        for row in rows[1:]:
            # Obtener las celdas de la fila actual
            cells = row.find_all(['th', 'td'])
    
            # La primera celda de cada fila contiene la hora
            hora = clean_text(cells[0].text)
    
            for dia, materia, materia_data in zip(dias_semana, cells[1:], cells[1:]):
                materia_text_list = materia.find_all('span', style='color:#1569C7; font-size:10px;')
                materia_data_text_list = materia_data.find_all('span', style='color:#FFFFFF;')
    
                # Procesar el texto de materia
                materia_text = [clean_text(span.text) for span in materia_text_list]
    
                # Procesar el texto de materia_data si es necesario
                materia_data_text = [clean_text(span.text) for span in materia_data_text_list]
    
                if dia not in horario_json:
                    horario_json[dia] = {}
    
                if materia_text:
                    horario_json[dia][hora] = {'materia': materia_text, 'materia_data': materia_data_text}
                else:
                    horario_json[dia][hora] = {'materia': '', 'materia_data': materia_data_text}
    
        return horario_json

    horario_tables = soup.find_all('table', {'class': 'tabla', 'style': 'font-size:10px;', 'width': '100%'})

    horario_final = {}
    for table in horario_tables:
        horario_dia = parse_horario_table(table)
        horario_final.update(horario_dia)

    # Convertir el horario final a JSON
    # horario_json = json.dumps(horario_final, ensure_ascii=False, indent=2)

    return horario_final

def get_student(sesion):
    # URLs de login y home
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/tiras'

    try:
        # Obtener la página de tiras de materias
        response_home = sesion.get(url_home)
        response_home.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

    soup = BeautifulSoup(response_home.content, 'html.parser')

    # Buscar la tabla de tiras de materias
    materias_table = soup.find('table', {'class': 'tabla'})
    if materias_table is None:
        raise ValueError("No se encontró ninguna tabla con los atributos especificados en el documento HTML.")

    def no_contiene_correo(tag):
        return tag.name == 'td' and not tag.text.strip().startswith("Guía para activar el correo:")

    etiquetas_td_k = soup.find_all(no_contiene_correo, {'class': ['naranja', 'azul']})

    etiquetas_td = soup.find_all(['td', 'th'], {'class': ['gris', 'rojo'], 'colspan': False})

    def clean_key(key):
        # Quitar acentos de la clave
        key_without_accents = unidecode(key)
        # Reemplazar los dos puntos con otro carácter (por ejemplo, guion bajo)
        key_cleaned = key_without_accents.replace(':', '')
        key_cleaned = key_cleaned.replace('del', '')
        key_cleaned = key_cleaned.replace('de', '')
        key_cleaned = key_cleaned.replace(' ', '')
        return key_cleaned

    # Crear un diccionario para almacenar los datos limpios en las claves
    data_cleaned = {}
    count = 0

    # Iterar sobre las claves originales y sus valores, limitando a los primeros 25
    for k, v in zip(etiquetas_td_k, etiquetas_td):
        # Limpiar la clave y agregar al diccionario
        key_cleaned = clean_key(k.text.strip())
        data_cleaned[key_cleaned] = v.text.strip()
        count += 1
        if count == 25:
            break

    # Guardar el diccionario limpio en un archivo JSON en la carpeta 'Data'
    if platform == 'android' or platform == 'ios':
        data_folder = storagepath.get_documents_dir()
    else:
        data_folder = os.path.join(os.getcwd(), 'Data')

    os.makedirs(data_folder, exist_ok=True)
    json_file_path = os.path.join(data_folder, 'data_cleaned.json')

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data_cleaned, file, ensure_ascii=False, indent=2)

    print(f"Extracción y guardado completados con éxito en {json_file_path}.")
    return data_cleaned

def save_file(data, file_name):
    """Guarda los datos en un archivo JSON."""
    if platform == 'android' or platform == 'ios':
        data_folder = storagepath.get_documents_dir()
    else:
        data_folder = os.path.join(os.getcwd(), 'Data')

    os.makedirs(data_folder, exist_ok=True)
    json_file_path = os.path.join(data_folder, file_name)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"Extracción y guardado completados con éxito en {json_file_path}.")
 