import requests

def login_ceti(registro, password):
    url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
    url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/horario'

    datos_post = {
        'registro': registro,
        'password': password
    }

    sesion = requests.Session()
    response_login = sesion.post(url_login, data=datos_post)

    # Verificar si el login fue exitoso
    if response_login.status_code == 200:
        # Intentar acceder a la página de inicio para verificar si el login fue exitoso
        response_home = sesion.get(url_home)
        if response_home.url == url_home:
            print("Login exitoso")
            return sesion
        else:
            print(f"Login fallido: No se pudo acceder a la página de inicio. URL: {response_home.url}")
            return None
    else:
        print(f"Login fallido: {response_login.status_code}, URL: {response_login.url}")
        return None

def logout_ceti(sesion):
    if sesion is None:
        return False
    url_logout = 'https://ase1.ceti.mx/tecnologo/tgoalumno/salir'
    response_logout = sesion.get(url_logout)

    if response_logout.status_code == 200:
        print("Logout exitoso de cierrre **********")
        return True
    else:
        print(f"*****Logout fallido: {response_logout.status_code}, URL: {response_logout.url}")
        return False