import json
import requests
from bs4 import BeautifulSoup
import os
from kivy.utils import platform
from plyer import storagepath

# Desactivar la depuración en Kivy
#kivy.logger.Logger.setLevel('info')

def clean_text(text):
    return text.strip().replace('\xa0', '')

def parse_horario_table(table):
    horario_json = {}
    rows = table.find_all('tr')
 
    dias_semana = [clean_text(th.text) for th in rows[0].find_all('th')]
    
    # Iterar sobre las filas de la tabla, excluyendo la primera fila (encabezados de días)
    for row in rows[1:]:
        # Obtener las celdas de la fila actual
        cells = row.find_all(['th', 'td'])
        # La primera celda de cada fila contiene la hora
        hora = clean_text(cells[0].text)
        
        for dia, materia, materia_data in zip(dias_semana, cells[1::2], cells[2::2]):
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

def obtener_horario(sesion, registro, password):
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/horario'
    response_home = sesion.get(url_home)
    soup = BeautifulSoup(response_home.content, 'html.parser')

    horario_tables = soup.find_all('table', {'class': 'tabla', 'style': 'font-size:10px;', 'width': '100%'})

    horario_final = {}
    for table in horario_tables:
        horario_dia = parse_horario_table(table)
        horario_final.update(horario_dia)

    # Convertir el horario final a JSON
    horario_json = json.dumps(horario_final, ensure_ascii=False, indent=2)

    # Guardar el archivo JSON en la carpeta 'Data'
    if platform == 'android' or platform == 'ios':
        data_folder = storagepath.get_documents_dir()
    else:
        data_folder = os.path.join(os.getcwd(), 'Data')

    os.makedirs(data_folder, exist_ok=True)
    json_file_path = os.path.join(data_folder, 'horario.json')

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(horario_json)

    print(f"Archivo JSON guardado en: {json_file_path}")