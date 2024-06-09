from PyQt5 import QtWidgets, uic


qtCreatorFile = "UI/HistorialVentas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class HistorialVentas(QtWidgets.QMainWindow):
    def __init__(self):
        super(HistorialVentas, self).__init__()
        uic.loadUi("UI/HistorialVentas.ui", self)
        self.btnRegresar.clicked.connect(self.regresar)

        self.show()

    def regresar(self):

        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
