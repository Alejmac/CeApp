from Model.login_Model import login_ceti

class LoginViewModel:
    def login(self, registro, password):
        return login_ceti(registro, password)