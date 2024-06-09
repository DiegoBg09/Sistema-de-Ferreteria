from PyQt5 import QtWidgets, uic
from Controlador.GestionGastos import *

aGto = GestionGastos()

class GestionVenta(QtWidgets.QMainWindow):
    def __init__(self):
        super(GestionVenta, self).__init__()
        uic.loadUi("UI/GestionVentas.ui", self)

        self.btnAgregarG.clicked.connect(self.agregar)
        self.btnCalcularG.clicked.connect(self.calcular)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()

    def obtenerSueldos(self):
        return self.txtSueldos.text()

    def obtenerImpuestos(self):
        return self.txtImpuestos.text()

    def obtenerSeguros(self):
        return self.txtSeguros.text()

    def obtenerServicios(self):
        return self.txtServicios.text()

    def limpiarTabla(self):
        self.tblGastos.clearContents()
        self.tblGastos.setRowCount(0)

    def valida(self):
        if self.txtSueldos.text() == "":
            self.txtSueldos.setFocus()
            return "Sueldos...!"

        if self.txtImpuestos.text() == "":
            self.txtImpuestos.setFocus()
            return "Impuestos...!"

        if self.txtSeguros.text() == "":
            self.txtSeguros.setFocus()
            return "Seguros...!"

        if self.txtServicios.text() == "":
            self.txtServicios.setFocus()
            return "Servicios...!"

        else:
            return ""

    def listar(self):
        self.tblGastos.setRowCount(aGto.tamanoGestionGasto())
        self.tblGastos.setColumnCount(4)
        for i in range(aGto.tamanoGestionGasto()):
            self.tblGastos.setItem(i, 0, QtWidgets.QTableWidgetItem(aGto.devolverGasto(i).getSueldos()))
            self.tblGastos.setItem(i, 1, QtWidgets.QTableWidgetItem(aGto.devolverGasto(i).getImpuestos()))
            self.tblGastos.setItem(i, 2, QtWidgets.QTableWidgetItem(aGto.devolverGasto(i).getSeguros()))
            self.tblGastos.setItem(i, 3, QtWidgets.QTableWidgetItem(aGto.devolverGasto(i).getServicios()))

    def limpiarControles(self):
        self.txtSueldos.clear()
        self.txtImpuestos.clear()
        self.txtSeguros.clear()
        self.txtServicios.clear()

    def agregar(self):
        if self.valida() == "":
            objGto = Gasto(self.obtenerSueldos(), self.obtenerImpuestos(), self.obtenerSeguros(), self.obtenerServicios())
            aGto.adicionaGasto(objGto)
            aGto.grabar()
            self.listar()
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Gasto", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def calcular(self):
        total_sueldos = float(self.obtenerSueldos())
        total_impuestos = float(self.obtenerImpuestos())
        total_seguros = float(self.obtenerSeguros())
        total_servicios = float(self.obtenerServicios())

        total_general = total_sueldos + total_impuestos + total_seguros + total_servicios

        self.txtTotal.setText(str(total_general))
        self.limpiarControles()

    def eliminar(self):
        if aGto.tamanoGestionGasto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Gasto", "No existen gastos a eliminar...!!")
        else:
            fila = self.tblGastos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                sueldos = self.tblGastos.item(indiceFila, 0)
                pos = aGto.buscarGasto(sueldos)
                aGto.eliminarGasto(pos)
                aGto.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Gasto", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
