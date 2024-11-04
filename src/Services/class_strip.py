import json
import requests
from bs4 import BeautifulSoup
import os

url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/tiras'

def get_tira_materias(registro, password):
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

# Ejemplo de uso
#registro = '21110191'
##password = '123asdzX'
#materias_asignadas = get_tira_materias(registro, password)

# Guardar las materias asignadas en un archivo JSON en la carpeta 'Data'
#if materias_asignadas is not None:
  #  data_folder = os.path.join(os.getcwd(), 'Data')
 #   os.makedirs(data_folder, exist_ok=True)
  #  json_file_path = os.path.join(data_folder, 'materias_asignadas.json')
#
  #  with open(json_file_path, 'w', encoding='utf-8') as json_file:
  #      json.dump(materias_asignadas, json_file, indent=2, ensure_ascii=False)

  #  print(f"Archivo JSON guardado en: {json_file_path}")

# Imprimir las materias asignadas en formato JSON
#print(json.dumps(materias_asignadas, indent=2, ensure_ascii=False))