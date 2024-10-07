from flet import app, Page
from View.first import FirstView

class Main:
    def __init__(self):
        self.first_view = FirstView()

    def run(self, page: Page):
        self.first_view.build(page)

# Ejemplo de uso
def main(page: Page):
    app_main = Main()
    app_main.run(page)

app(target=main)