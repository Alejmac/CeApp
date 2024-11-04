import json
import requests
from bs4 import BeautifulSoup
import os
from kivy.utils import platform
from plyer import storagepath
from unidecode import unidecode

def obtener_data(registro, password):
    # URLs de login y home
    url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/tiras'
    
    # Datos de acceso
    datos_post = {'registro': registro, 'password': password}

    try:
        # Iniciar sesión
        sesion = requests.Session()
        response_login = sesion.post(url_login, data=datos_post)
        response_login.raise_for_status()

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

    def clean_text(text):
        """Función para limpiar texto eliminando caracteres no deseados."""
        return text.replace('\xa0', '').replace('\n', '').strip() or "0"

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

# Ejemplo de uso
#if __name__ == "__main__":
 #   registro = '21110191'
   # password = '123asdzX'
  #  obtener_data(registro, password)