from flet import app, Page
from View.login_View import LoginView

class Main:
    def __init__(self):
        self.login_view = LoginView()

    def run(self, page: Page):
        self.login_view.build(page)

# Ejemplo de uso
def main(page: Page):
    app_main = Main()
    app_main.run(page)

app(target=main)