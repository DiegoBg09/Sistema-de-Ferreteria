from PyQt5 import QtWidgets, QtCore, uic
from Controlador.GestionProveedor import *

aPrv = GestionProveedor()

class VentanaProveedores(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaProveedores, self).__init__()
        uic.loadUi("UI/GestionProveedores.ui", self)

        self.btnRegresar.clicked.connect(self.regresar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()

    
    def obtenerProveedor(self):
        return self.txtProveedor.text()

    def obtenerCorreo(self):
        return self.txtCorreo.text()

    def obtenerRuc(self):
        return self.txtRuc.text()

    def obtenerFechaSalida(self):
        return self.dtFechSalida.date().toString('dd/MM/yyyy')

    def obtenerSuministro(self):
        return self.txtSuministro.text()

    def obtenerFechaEntrega(self):
        return self.dtFechEntrega.date().toString('dd/MM/yyyy')

    def obtenerContacto(self):
        return self.txtContacto.text()

    def obtenerEstado(self):
        return self.cboEstado.currentText()
    
    def limpiarTabla(self):
        self.tblProveedor.clearContents()
        self.tblProveedor.setRowCount(0)

    from PyQt5.QtCore import QDate

    def valida(self):
        if self.txtProveedor.text() == "":
            self.txtProveedor.setFocus()
            return "Proveedor del Producto...!"

        if self.txtCorreo.text() == "":
            self.txtCorreo.setFocus()
            return "Correo del Proveedor...!"

        if self.txtRuc.text() == "":
            self.txtRuc.setFocus()
            return "RUC del Proveedor...!"

        if self.dtFechSalida.date().toString('dd/MM/yyyy') == "":
            return "Fecha de Salida del Proveedor...!"

        if self.txtSuministro.text() == "":
            self.txtSuministro.setFocus()
            return "Suministro del Proveedor...!"

        if self.dtFechEntrega.date().toString('dd/MM/yyyy') == "":
            return "Fecha de Entrega del Proveedor...!"

        if self.txtContacto.text() == "":
            self.txtContacto.setFocus()
            return "Contacto del Proveedor...!"

        if self.cboEstado.currentText() == "":
            self.cboEstado.setCurrentIndex(0)
            return "Estado del Proveedor...!"

        return ""
    
    def listar(self):
        self.tblProveedor.setRowCount(aPrv.tamanoGestionProveedor())
        self.tblProveedor.setColumnCount(8)

        for i in range(aPrv.tamanoGestionProveedor()):
            self.tblProveedor.setItem(i, 0, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getProveedor()))
            self.tblProveedor.setItem(i, 1, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getCorreo()))
            self.tblProveedor.setItem(i, 2, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getRuc()))
            self.tblProveedor.setItem(i, 3, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getFechaSalida()))
            self.tblProveedor.setItem(i, 4, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getSuministro()))
            self.tblProveedor.setItem(i, 5, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getFechaEntrega()))
            self.tblProveedor.setItem(i, 6, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getContacto()))
            self.tblProveedor.setItem(i, 7, QtWidgets.QTableWidgetItem(aPrv.devolverProveedor(i).getEstado()))

    def limpiarControles(self):
        self.txtProveedor.clear()
        self.txtCorreo.clear()
        self.txtRuc.clear()
        self.dtFechSalida.setDate(QtCore.QDate.currentDate())
        self.txtSuministro.clear()
        self.dtFechEntrega.setDate(QtCore.QDate.currentDate())
        self.txtContacto.clear()
        self.cboEstado.setCurrentIndex(0)


    def registrar(self):
        if self.valida() == "":
            objPrv = Proveedor(self.obtenerProveedor(), self.obtenerCorreo(), self.obtenerRuc(),
                            self.obtenerFechaSalida(), self.obtenerSuministro(),
                            self.obtenerFechaEntrega(), self.obtenerContacto(),
                            self.obtenerEstado())

            proveedor = self.obtenerProveedor()

            if aPrv.buscarProveedor(proveedor) == -1:
                aPrv.adicionaProveedor(objPrv)
                aPrv.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "El proveedor ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def editar(self):
        if aPrv.tamanoGestionProveedor() == 0:
            QtWidgets.QMessageBox.information(self,"Modificar Proveedor", "No existen proveedores a modificar..!!")
        else:
            proveedor, _ = QtWidgets.QInputDialog.getText(self, "Modificar Proveedor", "Ingrese el proveedor a modificar")
            pos = aPrv.buscarProveedor(proveedor)
            if pos != -1:
                objProveedor = aPrv.devolverProveedor(pos)
                self.btnEditar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtProveedor.setText(objProveedor.getProveedor())
                self.txtProveedor.setVisible(False)
                self.lblProveedor.setVisible(False)
                self.txtCorreo.setText(objProveedor.getCorreo())
                self.txtRuc.setText(objProveedor.getRuc())
                fecha_salida = QtCore.QDate.fromString(objProveedor.getFechaSalida(), 'dd/MM/yyyy')
                self.dtFechSalida.setDate(fecha_salida)
                self.txtSuministro.setText(objProveedor.getSuministro())
                fecha_entrega = QtCore.QDate.fromString(objProveedor.getFechaEntrega(), 'dd/MM/yyyy')
                self.dtFechEntrega.setDate(fecha_entrega)
                self.txtContacto.setText(objProveedor.getContacto())
                self.cboEstado.setCurrentText(objProveedor.getEstado())

    def grabar(self):
        pos = aPrv.buscarProveedor(self.obtenerProveedor())
        objProveedor = aPrv.devolverProveedor(pos)
        objProveedor.setCorreo(self.obtenerCorreo())
        objProveedor.setRuc(self.obtenerRuc())
        objProveedor.setFechaSalida(self.obtenerFechaSalida()) 
        objProveedor.setSuministro(self.obtenerSuministro())
        objProveedor.setFechaEntrega(self.obtenerFechaEntrega())
        objProveedor.setContacto(self.obtenerContacto())
        objProveedor.setEstado(self.obtenerEstado())
        self.btnEditar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aPrv.grabar()
        self.listar()
        self.txtProveedor.setVisible(True)
        self.lblProveedor.setVisible(True)

    def eliminar(self):
        if aPrv.tamanoGestionProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Proveedor", "No existen proveedores a eliminar...!!")
        else:
            fila = self.tblProveedor.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProveedor.item(indiceFila, 0)
                pos = aPrv.buscarProveedor(codigo)
                aPrv.eliminarProveedor(pos)
                aPrv.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Proveedor", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):

        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()

