from PyQt5 import QtWidgets, uic
from Vista.MenuPrincipal import MenuPrincipal

qtCreatorFile = "UI/login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("UI/login.ui", self)

        self.btnLogin.clicked.connect(self.open_menu)
        self.show()

    def open_menu(self):
        usuario = self.txtUser.text()
        contrasena = self.txtPass.text()

        if (usuario == "admin1" and contrasena == "pass1"):

            self.menu_principal = MenuPrincipal()
            self.menu_principal.show()
            self.close() 

