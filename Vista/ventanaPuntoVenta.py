from PyQt5 import QtWidgets, QtCore, uic
from Controlador.GestionVentas import *

aVta = GestionVentas()

class VentanaPuntoVenta(QtWidgets.QMainWindow):

    def __init__(self):
        super(VentanaPuntoVenta, self).__init__()
        uic.loadUi("UI/PuntoVenta.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()

    def obtenerNroCompra(self):
        return self.txtNroCompra.text()

    def obtenerIdCliente(self):
        return self.txtIdCliente.text()

    def obtenerFechaPago(self):
        return self.dtFechPago.date().toString('dd/MM/yyyy')

    def obtenerModoPago(self):
        return self.cboModoPago.currentText()

    def limpiarTabla(self):
        self.tblCompra.clearContents()
        self.tblCompra.setRowCount(0)

    def valida(self):
        if self.txtNroCompra.text() == "":
            self.txtNroCompra.setFocus()
            return "Número de compra...!"

        if self.txtIdCliente.text() == "":
            self.txtIdCliente.setFocus()
            return "ID Cliente...!"

        if self.dtFechPago.date().toString('dd/MM/yyyy') == "":
            return "Fecha de Pago...!"

        if self.cboModoPago.currentText() == "":
            self.cboModoPago.setCurrentIndex(0)
            return "Modo de pago...!"

        else:
            return ""

    def listar(self):
        self.tblCompra.setRowCount(aVta.tamanoGestionVenta())
        self.tblCompra.setColumnCount(4)
        for i in range(aVta.tamanoGestionVenta()):
            self.tblCompra.setItem(i, 0, QtWidgets.QTableWidgetItem(aVta.devolverVenta(i).getNroCompra()))
            self.tblCompra.setItem(i, 1, QtWidgets.QTableWidgetItem(aVta.devolverVenta(i).getIdCliente()))
            self.tblCompra.setItem(i, 2, QtWidgets.QTableWidgetItem(aVta.devolverVenta(i).getFechaPago()))
            self.tblCompra.setItem(i, 3, QtWidgets.QTableWidgetItem(aVta.devolverVenta(i).getModoPago()))

    def limpiarControles(self):
        self.txtNroCompra.clear()
        self.txtIdCliente.clear()
        self.dtFechPago.setDate(QtCore.QDate.currentDate())
        self.cboModoPago.setCurrentIndex(0)

    def registrar(self):
        if self.valida() == "":
            objVta = Venta(self.obtenerNroCompra(), self.obtenerIdCliente(), self.obtenerFechaPago(), self.obtenerModoPago())
            nro_compra = self.obtenerNroCompra()
            if aVta.buscarVenta(nro_compra) == -1:
                aVta.adicionaVenta(objVta)
                aVta.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Venta", "El número de compra ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Venta", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def cancelar(self):
        if aVta.tamanoGestionVenta() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Venta", "No existen ventas a eliminar...!!")
        else:
            fila = self.tblCompra.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                nro_compra = self.tblCompra.item(indiceFila, 0)
                pos = aVta.buscarVenta(nro_compra)
                aVta.eliminarVenta(pos)
                aVta.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Venta", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
