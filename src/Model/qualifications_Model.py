import os
import json

def cargar_calificaciones(json_file_path):
    if not os.path.exists(json_file_path):
        print(f"El archivo {json_file_path} no existe.")
        return None

    # Leer el archivo JSON
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        calificaciones = json.load(json_file)

    # Crear un diccionario de clave-valor
    calificaciones_dict = {}
    for clave, valores in calificaciones.items():
        calificaciones_dict[clave] = valores

    return calificaciones_dict

# Ejemplo de uso
if __name__ == "__main__":
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'qualifications.json')
    calificaciones = cargar_calificaciones(json_file_path)
    if calificaciones:
        for clave, valores in calificaciones.items():
            print(f"Clave: {clave}")
            for k, v in valores.items():
                print(f"  {k}: {v}")